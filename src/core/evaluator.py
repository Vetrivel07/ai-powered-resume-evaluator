from src.llm.prompts import HR_PROMPT, ATS_PROMPT
from src.llm.openai_client import upload_pdf_for_input, analyze_pdf_with_prompt
from src.core.parsing import parse_json_loose

def evaluate_hr(jd_text: str, uploaded_pdf):
    pdf_bytes = uploaded_pdf.getvalue()
    file_id = upload_pdf_for_input(pdf_bytes, uploaded_pdf.name)
    return analyze_pdf_with_prompt(HR_PROMPT, jd_text, file_id)

def evaluate_ats(jd_text: str, uploaded_pdf):
    pdf_bytes = uploaded_pdf.getvalue()
    file_id = upload_pdf_for_input(pdf_bytes, uploaded_pdf.name)
    raw = analyze_pdf_with_prompt(ATS_PROMPT + "\nReturn ONLY JSON.", jd_text, file_id)
    ok, out = parse_json_loose(raw)
    return ok, out, raw
