from lib.model_client import ModelClientError, generate_answer
from lib.prompt_builder import build_rag_prompt
from lib.response_formatter import (
    format_fallback_response,
    format_sources,
    format_success_response,
)
from lib.retrieval import DEFAULT_TOP_K, retrieve_context


def answer_question(
    question,
    retriever=None,
    prompt_builder=None,
    model_client=None,
    top_k=DEFAULT_TOP_K,
):
    """Run the full RAG workflow for a validated question."""
    # TODO: Use provided dependencies when passed, otherwise use default helpers.
    # TODO: Retrieve context before building the prompt.
    # TODO: Return fallback response and do not call the model when context is empty.
    # TODO: Build the prompt.
    # TODO: Call the model client.
    # TODO: Raise ModelClientError if the model answer is blank or unusable.
    # TODO: Return formatted success response with answer and sources.
    raise NotImplementedError("Implement answer_question().")