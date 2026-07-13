from backend.analyzer import analyze_code
from backend.java_analyzer import analyze_java
from backend.c_analyzer import analyze_c
from backend.cpp_analyzer import analyze_cpp
from backend.chatbot import get_ai_response
from backend.pdf_generator import generate_pdf

import streamlit as st

from analyzer import analyze_code
from java_analyzer import analyze_java
from c_analyzer import analyze_c
from cpp_analyzer import analyze_cpp

st.set_page_config(page_title="AI Code Flow Mapper", layout="wide")

st.title("AI Code Flow Mapper")

language = st.selectbox(
    "Select Language",
    ["python", "java", "c", "cpp"]
)

code = st.text_area("Paste your code here", height=300)

if st.button("Analyze"):

    if language == "python":
        result = analyze_code(code)

    elif language == "java":
        result = analyze_java(code)

    elif language == "c":
        result = analyze_c(code)

    else:
        result = analyze_cpp(code)

    st.subheader("Analysis")
    st.json(result)
