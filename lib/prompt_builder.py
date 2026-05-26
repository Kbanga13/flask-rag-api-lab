def format_context_chunk(chunk):
    """Format one retrieved chunk for the prompt context block."""
    # TODO: Include source_id, title, category, section, and text.
    raise NotImplementedError("Implement format_context_chunk().")


def build_rag_prompt(question, context_chunks):
    """Build a structured RAG prompt from a question and retrieved context."""
    # TODO: Validate that the question is not blank.
    # TODO: Validate that context_chunks contains usable text.
    # TODO: Build a prompt with these sections:
    #       Instructions:
    #       Context:
    #       Question:
    #       Response Requirements:
    # TODO: Tell the model to use only approved context and avoid unsupported claims.
    raise NotImplementedError("Implement build_rag_prompt().")