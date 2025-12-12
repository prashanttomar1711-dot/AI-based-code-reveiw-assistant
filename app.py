import streamlit as st
from review import review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("AI-based Code Review Assistant — Demo")
st.markdown("Upload a file or paste code below. The assistant will return a structured review using an LLM.")

with st.sidebar:
    st.header("Settings")
    language = st.selectbox("Language", ["python", "javascript", "java", "c", "cpp", "go"], index=0)
    max_tokens = st.slider("Max tokens for model response", 200, 2000, 800)

uploaded = st.file_uploader("Upload source file (optional)", type=["py", "js", "java", "c", "cpp", "go", "txt"])

code_input = st.text_area("Or paste code here", height=300)

if uploaded is not None and code_input.strip() == "":
    code_input = uploaded.getvalue().decode("utf-8")

if st.button("Run Review"):
    if not code_input.strip():
        st.error("Please paste code or upload a file.")
    else:
        with st.spinner("Asking AI to review... (may take a few seconds)"):
            try:
                review = review_code(code_input, language=language)
                st.subheader("Review Result")
                st.markdown("---")
                st.code(review, language="text")
            except Exception as e:
                st.error(f"Error while reviewing: {e}")
