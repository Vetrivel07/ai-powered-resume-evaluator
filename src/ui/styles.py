APP_CSS = """
<style>
.block-container { max-width: 800px; padding-top: 20px; }
h1, h2, h3 { color:#2c3e50; }
label, .stTextArea label, .stFileUploader label { font-weight:600; color:#34495e; }
.stTextArea textarea {
  width:100%; padding:12px; border:1px solid #ccd1d9; border-radius:6px;
  font-size:14px; resize:vertical;
}
.stFileUploader div[data-testid="stFileUploadDropzone"] {
  border:1px solid #ccd1d9; border-radius:6px; background:#fff;
}
.stButton > button {
  background:#1e90ff; color:#fff; padding:10px 20px; border:0; border-radius:6px;
  transition:background-color .3s ease; font-size:14px;
}
.stButton > button:hover { background:#0d6efd; }
.result-box {
  margin-top: 20px; padding: 16px; background:#ecf0f1; border-left:6px solid #3498db; border-radius:6px;
}
</style>
"""
