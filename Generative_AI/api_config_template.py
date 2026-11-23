"""
Gemini API configuration template (no keys in this file).

How to provide the key
----------------------
The key is never written in code or committed to GitHub. Use one of these:

1. Google Colab (recommended for the team):
   Open the key icon ("Secrets") in the left sidebar, add a secret named
   GEMINI_API_KEY, paste your key as its value, and enable notebook access.

2. Local Jupyter / VS Code:
   Copy `.env.example` (repository root) to `.env` and put your key after
   GEMINI_API_KEY=. The `.env` file is listed in `.gitignore`.

3. Any environment:
   Set the environment variable GEMINI_API_KEY before starting Python.

Get a free key from Google AI Studio: https://aistudio.google.com/apikey

Usage
-----
    from api_config_template import get_client, GENERATION_SETTINGS
    client = get_client()
"""

import os

# Model and generation settings shared by every prompt template, so that
# Template 1 and Template 2 are compared under the same conditions.
DEFAULT_MODEL = "gemini-3.6-flash"
MODEL_NAME = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)

GENERATION_SETTINGS = {
    # Low temperature keeps briefings factual and makes reruns similar.
    "temperature": 0.2,
    "max_output_tokens": 2048,
}

# Gemini 3 models "think" before answering. A briefing only rewrites given
# facts, so the lowest thinking level is used to keep answers fast.
THINKING_LEVEL = "minimal"

KEY_NAME = "GEMINI_API_KEY"


def _key_from_colab():
    """Return the key from Colab Secrets, or None when not running in Colab."""
    try:
        from google.colab import userdata  # only exists inside Colab
    except ImportError:
        return None
    try:
        return userdata.get(KEY_NAME)
    except Exception:
        return None


def _key_from_dotenv():
    """Load a local .env file (if python-dotenv is installed) and read the key."""
    try:
        from dotenv import find_dotenv, load_dotenv
    except ImportError:
        return None
    load_dotenv(find_dotenv(usecwd=True))
    return os.environ.get(KEY_NAME)


def get_api_key():
    """Find the key in the environment, Colab Secrets, or a local .env file."""
    key = os.environ.get(KEY_NAME) or _key_from_colab() or _key_from_dotenv()
    if not key:
        raise RuntimeError(
            f"{KEY_NAME} was not found. Add it to Colab Secrets or to a local "
            ".env file (see the instructions at the top of api_config_template.py)."
        )
    return key


def get_client():
    """Create a Gemini client. The key is passed in memory and never printed."""
    from google import genai

    return genai.Client(api_key=get_api_key())


def has_api_key():
    """True when a key is available, used to skip live calls when there is none."""
    try:
        get_api_key()
        return True
    except RuntimeError:
        return False
