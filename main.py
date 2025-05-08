from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from pdf_utils import extract_text_from_pdf
from gemini_utils import ask_gemini

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/upload", response_class=HTMLResponse)
async def upload_files(request: Request, files: list[UploadFile] = File(...)):
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
    return templates.TemplateResponse("index.html", {"request": request, "answer": "Fajlovi uspešno sačuvani. Možete sada postavljati pitanja."})

@app.post("/ask", response_class=HTMLResponse)
async def ask_question(
    request: Request,
    question: str = Form(...)
):
    documents = []
    
    for filename in os.listdir(UPLOAD_DIR):
        if filename.endswith(".pdf"):
            file_path = os.path.join(UPLOAD_DIR, filename)
            pdf_text = extract_text_from_pdf(file_path)
            documents.append((filename, pdf_text))

    if not documents:
        return templates.TemplateResponse("index.html", {"request": request, "answer": "Nema učitanih PDF dokumenata. Prvo ih postavite."})

    # Kombinuj sve dokumente u jedan veliki kontekst
    context = "\n\n".join([f"DOKUMENT: {name}\n{content}" for name, content in documents])

    # Pitaj AI
    answer = ask_gemini(question, context)

    # Forma odgovora
    response = f"Pozdrav! našao sam odgovor na tvoje pitanje: \n\n{answer.strip()}"

    return templates.TemplateResponse("index.html", {"request": request, "answer": response})
