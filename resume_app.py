# -*- coding: utf-8 -*-

import streamlit as st
from docxtpl import DocxTemplate
import json
import tempfile

st.set_page_config(page_title="Resume & Cover Letter Generator", layout="centered")
st.title("📄 Resume & Cover Letter Generator")
st.markdown("Paste your JSON below and download your tailored documents.")

json_input = st.text_area("Paste your resume JSON here", height=400)

if st.button("Generate Documents"):
    try:
        context = json.loads(json_input)

        # Generate Resume
        resume_doc = DocxTemplate("resume_template.docx")
        resume_doc.render(context)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_resume:
            resume_doc.save(tmp_resume.name)
            st.success("Resume generated successfully!")
            st.download_button("📥 Download Resume", data=open(tmp_resume.name, "rb").read(), file_name="Tailored_Resume.docx")

        # Generate Cover Letter
        cover_doc = DocxTemplate("cover_letter_template.docx")
        cover_doc.render(context)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_cover:
            cover_doc.save(tmp_cover.name)
            st.success("Cover letter generated successfully!")
            st.download_button("📥 Download Cover Letter", data=open(tmp_cover.name, "rb").read(), file_name="Tailored_Cover_Letter.docx")

    except Exception as e:
        st.error(f"Error: {e}")