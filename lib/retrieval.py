CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "customer_success_knowledge"
DEFAULT_TOP_K = 3


def get_chroma_collection(path=CHROMA_PATH, collection_name=COLLECTION_NAME):
    """Return a persistent Chroma collection for manual local testing."""
    # TODO: Import chromadb inside this function.
    # TODO: Create a PersistentClient using path.
    # TODO: Return get_or_create_collection(collection_name).
    raise NotImplementedError("Implement get_chroma_collection().")


def format_chroma_results(results):
    """Normalize Chroma query results into context chunk dictionaries.

    Chroma query results often look like:
        {
            "ids": [["chunk-1"]],
            "documents": [["Text"]],
            "metadatas": [[{"source_id": "SRC-1"}]],
            "distances": [[0.12]]
        }
    """
    # TODO: Handle nested Chroma result lists.
    # TODO: Skip missing or blank documents.
    # TODO: Return dictionaries with id, text, source_id, title, category,
    #       section, and distance keys.
    raise NotImplementedError("Implement format_chroma_results().")


def retrieve_context(question, collection=None, top_k=DEFAULT_TOP_K):
    """Retrieve context chunks for a user question.

    Tests may pass a fake collection. Manual use should call Chroma.
    """
    # TODO: Strip the question.
    # TODO: Use the provided collection or get_chroma_collection().
    # TODO: Call collection.query() with query_texts, n_results, and include.
    # TODO: Return normalized context chunks.
    raise NotImplementedError("Implement retrieve_context().")