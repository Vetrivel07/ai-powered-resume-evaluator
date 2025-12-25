import os
from dotenv import load_dotenv

DEFAULT_MODEL = "gpt-4o-mini"

def init_settings():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set")

def get_model() -> str:
    return os.getenv("OPENAI_MODEL", DEFAULT_MODEL)
