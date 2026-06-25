import requests

DEFAULT_MODEL_NAME = "llama3.2"
DEFAULT_BASE_URL = "http://localhost:11434"
DEFAULT_TIMEOUT = 60


class ModelClientError(Exception):
    """Raised when the local model service cannot return a usable answer."""


def generate_answer(prompt, model_name=DEFAULT_MODEL_NAME, base_url=DEFAULT_BASE_URL):
    """Send the prompt to a local Ollama model and return the generated answer."""
    if not isinstance(prompt, str) or not prompt.strip():
        raise ModelClientError("Prompt must be a non-empty string.")

    url = f"{base_url}/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise ModelClientError(f"Model request failed: {exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise ModelClientError("Model response was not valid JSON.") from exc

    if not isinstance(data, dict):
        raise ModelClientError("Model response was not a JSON object.")

    text = data.get("response")
    if not isinstance(text, str) or not text.strip():
        raise ModelClientError("Model response did not contain usable text.")

    return text.strip()
