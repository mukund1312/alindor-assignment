import streamlit as st
import json

from utils.pdfutils import extract_text_from_pdf
from utils.evaluation import evaluate_resume

st.title("Resume Review")

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = None

if "job_description" not in st.session_state:
    st.session_state["job_description"] = None

if "evaluation" not in st.session_state:
    st.session_state["evaluation"] = None

uploaded_file = st.file_uploader("Upload the resume (PDF)", type="pdf")

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.session_state["resume_text"] = resume_text
    with st.expander("Resume Text"):
        st.write(resume_text)

job_description = st.text_area("Job description")
if job_description is not None:
    st.session_state["job_description"] = job_description
    evaluate_button = st.button("Evaluate")

    if evaluate_button:
        evaluation = evaluate_resume(st.session_state["resume_text"], job_description)
        try:
            evaluation = json.loads(evaluation)
            st.session_state["evaluation"] = evaluation
            with st.expander("Evaluation"):
                st.text(evaluation)
        except:
            st.error("ERROR: Error in response format by LLM, Please reload the page and try again")
