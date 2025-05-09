import streamlit as st
from utils import extract_text_from_pdf
from resume_analyzer import analyze_resume
import os

st.set_page_config(page_title="📄 AI Resume Analyzer (Ollama)", layout="wide")
st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and match it with job descriptions using a local LLM (Ollama + LLaMA 3).")

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
with col2:
    job_description = st.text_area("Enter Job Description (optional):")

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume with Ollama..."):
            result = analyze_resume(resume_text, job_description)
            st.subheader("🔍 Analysis Result")
            st.write(result)
else:
    st.warning("Please upload a PDF resume.")
