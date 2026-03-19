"""core/level_detector.py — Classifies a user message into a technical level."""

import os
from openai import OpenAI
from dotenv import load_dotenv
from config.prompts import DETECTION_PROMPT, VALID_LEVELS

load_dotenv()  # carga las variables desde el archivo .env

_MODEL  = "@cf/meta/llama-3.1-8b-instruct"
_client = None  # initialized lazily on first use


def _get_client() -> OpenAI:
    """Create the Cloudflare client on first call (reads env vars at runtime)."""
    global _client
    if _client is None:
        account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")
        api_token  = os.environ.get("CLOUDFLARE_API_TOKEN", "")
        if not account_id or not api_token:
            raise EnvironmentError(
                "Missing credentials. Please set CLOUDFLARE_ACCOUNT_ID "
                "and CLOUDFLARE_API_TOKEN environment variables."
            )
        _client = OpenAI(
            api_key=api_token,
            base_url=f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1",
        )
    return _client


def detect_level(text: str) -> str:
    """
    Ask the LLM to classify the technical level of a user message.

    Returns one of: 'beginner', 'intermediate', 'advanced'.
    Falls back to 'intermediate' on any error or unexpected output.
    """
    try:
        response = _get_client().chat.completions.create(
            model=_MODEL,
            max_tokens=10,
            messages=[{"role": "user", "content": DETECTION_PROMPT + text}],
        )
        level = response.choices[0].message.content.strip().lower()
        return level if level in VALID_LEVELS else "intermediate"
    except Exception:
        return "intermediate"