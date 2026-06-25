CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "customer_success_knowledge"
DEFAULT_TOP_K = 3


def get_chroma_collection(path=CHROMA_PATH, collection_name=COLLECTION_NAME):
    """Return a persistent Chroma collection for manual local testing."""
    import chromadb

    client = chromadb.PersistentClient(path=path)
    return client.get_or_create_collection(collection_name)


def format_chroma_results(results):
    """Normalize Chroma query results into context chunk dictionaries."""
    if not results:
        return []

    def first(key):
        value = results.get(key) or []
        if value and isinstance(value, list) and isinstance(value[0], list):
            return value[0]
        return value

    ids = first("ids")
    documents = first("documents")
    metadatas = first("metadatas")
    distances = first("distances")

    chunks = []
    for index, document in enumerate(documents):
        if not document or not isinstance(document, str) or not document.strip():
            continue

        metadata = metadatas[index] if index < len(metadatas) and metadatas[index] else {}
        chunk_id = ids[index] if index < len(ids) else None
        distance = distances[index] if index < len(distances) else None

        chunks.append(
            {
                "id": chunk_id,
                "text": document.strip(),
                "source_id": metadata.get("source_id"),
                "title": metadata.get("title"),
                "category": metadata.get("category"),
                "section": metadata.get("section"),
                "distance": distance,
            }
        )

    return chunks


def retrieve_context(question, collection=None, top_k=DEFAULT_TOP_K):
    """Retrieve context chunks for a user question."""
    if not isinstance(question, str):
        return []

    cleaned = question.strip()
    if not cleaned:
        return []

    if collection is None:
        collection = get_chroma_collection()

    results = collection.query(
        query_texts=[cleaned],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    return format_chroma_results(results)
