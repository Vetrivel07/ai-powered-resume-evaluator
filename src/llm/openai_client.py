import os
from openai import OpenAI
from src.config import get_model

_client = None

def client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client

def upload_pdf_for_input(file_bytes: bytes, filename: str) -> str:
    # purpose user_data is documented for flexible file inputs
    f = client().files.create(
        file=(filename, file_bytes, "application/pdf"),
        purpose="user_data",
    )
    return f.id

def analyze_pdf_with_prompt(system_prompt: str, jd_text: str, pdf_file_id: str) -> str:
    # Responses API supports PDF file inputs via file_id
    resp = client().responses.create(
        model=get_model(),
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": system_prompt},
                {"type": "input_text", "text": f"Job Description:\n{jd_text}"},
                {"type": "input_file", "file_id": pdf_file_id},
            ],
        }],
    )
    return resp.output_text
