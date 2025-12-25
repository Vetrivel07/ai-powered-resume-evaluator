import streamlit as st

from src.config import init_settings
from src.ui.styles import APP_CSS
from src.core.evaluator import evaluate_hr, evaluate_ats

# Initialize config once (Streamlit reruns; guard with session_state)
if "settings_initialized" not in st.session_state:
    init_settings()
    st.session_state["settings_initialized"] = True

st.set_page_config(page_title="AI-Powered Resume Evaluator")
st.markdown(APP_CSS, unsafe_allow_html=True)

st.header("AI-Powered Resume Evaluator")

uploaded = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Job Description")

c1, c2 = st.columns(2)
hr_btn = c1.button("Tell Me About the Resume")
ats_btn = c2.button("Percentage match")

if uploaded:
    st.caption("PDF uploaded successfully.")

if hr_btn or ats_btn:
    if not uploaded or not jd_text.strip():
        st.error("Upload a PDF and paste a job description.")
    else:
        if hr_btn:
            with st.spinner("Analyzing your resume..."):
                text = evaluate_hr(jd_text, uploaded)
            st.success("Analysis complete.")
            st.subheader("Response")
            st.write(text)

        if ats_btn:
            with st.spinner("Reading resume and job description... Please wait."):
                ok, out, raw = evaluate_ats(jd_text, uploaded)

            st.success("Evaluation complete.")
            st.subheader("Response")

            if ok and isinstance(out, dict):
                st.markdown("### Percentage match")
                mp = out.get("match_percent")
                st.write(f"{mp}%" if mp is not None else "")

                st.markdown("### About the job")
                st.write(out.get("about_job", ""))

                st.markdown("### Your resume")
                st.write(out.get("your_resume", ""))

                st.markdown("### Summary")
                st.write(out.get("summary", ""))
            else:
                st.error("Model did not return valid JSON.")
                st.code(raw)
