# -*- coding: utf-8 -*-

import streamlit as st
from docxtpl import DocxTemplate
import json
import tempfile

st.set_page_config(page_title="Resume Tailor", layout="centered")

st.title("📄 Resume Tailoring App")
st.markdown("Paste your JSON below and download your tailored resume.")

json_input = st.text_area("Paste your resume JSON here", height=400)

if st.button("Generate Resume"):
    try:
        context = json.loads(json_input)
        doc = DocxTemplate("resume_template.docx")
        doc.render(context)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            doc.save(tmp.name)
            st.success("Resume generated successfully!")
            st.download_button("📥 Download Resume", data=open(tmp.name, "rb").read(), file_name="Tailored_Resume.docx")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.title("📝 Cover Letter Generator")
st.markdown("Paste the same JSON below to generate a tailored cover letter.")

json_input_cl = st.text_area("Paste your resume JSON here (for cover letter)", height=400)

if st.button("Generate Cover Letter"):
    try:
        context = json.loads(json_input_cl)
        doc = DocxTemplate("cover_letter_template.docx")
        doc.render(context)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            doc.save(tmp.name)
            st.success("Cover letter generated successfully!")
            st.download_button("📥 Download Cover Letter", data=open(tmp.name, "rb").read(), file_name="Tailored_Cover_Letter.docx")
    except Exception as e:
        st.error(f"Error: {e}")
