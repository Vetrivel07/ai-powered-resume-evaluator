import json

def parse_json_loose(text: str):
    """
    Returns: (ok: bool, out: dict|str)
    - Accepts raw JSON or ```json fenced output
    """
    cleaned = text.strip()
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    try:
        return True, json.loads(cleaned)
    except Exception:
        return False, text
