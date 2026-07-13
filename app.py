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

app = FastAPI(
    title="AI Code Flow Mapper API",
    version="1.0.0"
)

# CORS
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
    return {
        "status": "success",
        "message": "AI Code Flow Mapper Backend Running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(data: CodeInput):

    language = data.language.lower()

    if language == "python":
        return analyze_code(data.code)

    elif language == "java":
        return analyze_java(data.code)

    elif language == "c":
        return analyze_c(data.code)

    elif language == "cpp":
        return analyze_cpp(data.code)

    return {"error": "Unsupported language"}


@app.post("/chat")
def chat(data: ChatInput):
    return {
        "answer": get_ai_response(data.question)
    }


@app.post("/download-pdf")
def download_pdf(data: CodeInput):

    language = data.language.lower()

    if language == "python":
        analysis = analyze_code(data.code)

    elif language == "java":
        analysis = analyze_java(data.code)

    elif language == "c":
        analysis = analyze_c(data.code)

    elif language == "cpp":
        analysis = analyze_cpp(data.code)

    else:
        return {"error": "Unsupported language"}

    pdf_file = generate_pdf(analysis)

    return FileResponse(
        path=pdf_file,
        filename="analysis_report.pdf",
        media_type="application/pdf",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
