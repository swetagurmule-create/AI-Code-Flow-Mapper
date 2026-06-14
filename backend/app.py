from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from analyzer import analyze_code
from java_analyzer import analyze_java
from c_analyzer import analyze_c
from cpp_analyzer import analyze_cpp

from chatbot import get_ai_response
from pdf_generator import generate_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODELS ----------------

class CodeInput(BaseModel):
    code: str
    language: str = "python"

class ChatInput(BaseModel):
    question: str


# ---------------- ROUTES ----------------

@app.get("/")
def home():
    return {"message": "Backend Working"}


@app.post("/analyze")
def analyze(data: CodeInput):

    if data.language == "python":
        return analyze_code(data.code)

    elif data.language == "java":
        return analyze_java(data.code)

    elif data.language == "c":
        return analyze_c(data.code)

    elif data.language == "cpp":
        return analyze_cpp(data.code)

    return {"error": "Unsupported language"}


@app.post("/chat")
def chat(data: ChatInput):
    return {
        "answer": get_ai_response(data.question)
    }


# ---------------- PDF DOWNLOAD ----------------

@app.post("/download-pdf")
def download_pdf(data: CodeInput):

    if data.language == "python":
        analysis = analyze_code(data.code)

    elif data.language == "java":
        analysis = analyze_java(data.code)

    elif data.language == "c":
        analysis = analyze_c(data.code)

    elif data.language == "cpp":
        analysis = analyze_cpp(data.code)

    else:
        analysis = {"error": "Unsupported language"}

    pdf_file = generate_pdf(analysis)

    return FileResponse(
        path=pdf_file,
        filename="analysis_report.pdf",
        media_type="application/pdf"
    )
