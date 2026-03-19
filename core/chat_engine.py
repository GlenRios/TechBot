"""core/chat_engine.py — Builds the system prompt and calls Cloudflare Workers AI."""

import os
import traceback
import streamlit as st
from openai import OpenAI
from config.prompts import BASE_PROMPT, LEVEL_PROMPTS
from state.session import effective_level

_MODEL      = "@cf/meta/llama-3.1-8b-instruct"
_MAX_TOKENS = 1024
_client     = None


def _get_client() -> OpenAI:
    """Create the Cloudflare client on first call."""
    global _client
    if _client is None:
        account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")
        api_token  = os.environ.get("CLOUDFLARE_API_TOKEN", "")

        print(f"[DEBUG] _get_client — account_id={'SET' if account_id else 'MISSING'}")
        print(f"[DEBUG] _get_client — api_token={'SET'  if api_token  else 'MISSING'}")

        if not account_id or not api_token:
            raise EnvironmentError(
                "Faltan credenciales. Agrega CLOUDFLARE_ACCOUNT_ID y "
                "CLOUDFLARE_API_TOKEN en el archivo .env"
            )

        base_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1"
        print(f"[DEBUG] base_url = {base_url}")

        _client = OpenAI(api_key=api_token, base_url=base_url)
        print("[DEBUG] OpenAI client created ✓")

    return _client


def build_system_prompt(level: str) -> str:
    level_block = LEVEL_PROMPTS.get(level, LEVEL_PROMPTS["intermediate"])
    return BASE_PROMPT + level_block


def get_response() -> str:
    """
    Call Cloudflare Workers AI and return the full response as a string.
    (Non-streaming — easier to debug)
    """
    try:
        level  = effective_level()
        system = build_system_prompt(level)
        print(f"[DEBUG] get_response — level={level}")

        api_messages = [{"role": "system", "content": system}] + [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        print(f"[DEBUG] get_response — sending {len(api_messages)} messages")

        response = _get_client().chat.completions.create(
            model=_MODEL,
            max_tokens=_MAX_TOKENS,
            messages=api_messages,
            stream=False,
        )
        print("[DEBUG] get_response — API call succeeded ✓")

        return response.choices[0].message.content

    except Exception as e:
        print(f"[ERROR] get_response failed: {e}")
        traceback.print_exc()
        return f"⚠️ **Error al conectar con Cloudflare:** `{e}`"