def format_context_chunk(chunk):
    """Format one retrieved chunk for the prompt context block."""
    if not isinstance(chunk, dict):
        return ""

    source_id = chunk.get("source_id") or "UNKNOWN"
    title = chunk.get("title") or "Untitled"
    category = chunk.get("category") or "Uncategorized"
    section = chunk.get("section") or "General"
    text = (chunk.get("text") or "").strip()

    return (
        f"[Source: {source_id}] {title} "
        f"(Category: {category}, Section: {section})\n"
        f"{text}"
    )


def build_rag_prompt(question, context_chunks):
    """Build a structured RAG prompt from a question and retrieved context."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question must be a non-blank string.")

    if not context_chunks:
        raise ValueError("At least one context chunk is required.")

    usable_chunks = [
        chunk
        for chunk in context_chunks
        if isinstance(chunk, dict) and (chunk.get("text") or "").strip()
    ]
    if not usable_chunks:
        raise ValueError("Context chunks must contain usable text.")

    cleaned_question = question.strip()
    context_block = "\n\n".join(format_context_chunk(chunk) for chunk in usable_chunks)

    return (
        "Instructions:\n"
        "You are a customer success assistant. Use only the approved context "
        "below to answer the support representative's question. Do not invent "
        "details, policies, or guarantees that are not supported by the "
        "approved context. If the context does not contain enough information, "
        "say so clearly and identify what is missing.\n\n"
        "Context:\n"
        f"{context_block}\n\n"
        "Question:\n"
        f"{cleaned_question}\n\n"
        "Response Requirements:\n"
        "- Use only the approved context provided above.\n"
        "- Do not invent unsupported claims or policies.\n"
        "- If information is missing, state which detail is missing.\n"
        "- Answer concisely and accurately.\n"
        "- Refer to the relevant source IDs when helpful.\n"
    )
