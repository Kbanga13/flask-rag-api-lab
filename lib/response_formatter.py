FALLBACK_MESSAGE = (
    "The approved customer success documents do not contain enough information "
    "to answer that question. Review the relevant policy or contact a supervisor "
    "before acting on this request."
)


def format_sources(context_chunks):
    """Return source metadata for retrieved context chunks."""
    # TODO: Return unique source dictionaries.
    # TODO: Include id, title, category, section, and chunk_id.
    # TODO: Do not include full text or distance values in source entries.
    raise NotImplementedError("Implement format_sources().")


def format_success_response(answer, sources):
    """Return the successful RAG API response body."""
    # TODO: Return {"answer": cleaned_answer, "sources": sources_list}.
    raise NotImplementedError("Implement format_success_response().")


def format_fallback_response(question=None):
    """Return a safe response when there is not enough approved context."""
    # TODO: Return FALLBACK_MESSAGE with an empty sources list.
    raise NotImplementedError("Implement format_fallback_response().")


def format_error_response(error, message):
    """Return a standard error response body."""
    # TODO: Return {"error": error, "message": message}.
    raise NotImplementedError("Implement format_error_response().")