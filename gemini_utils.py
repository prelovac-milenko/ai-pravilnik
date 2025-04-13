import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question, context):
    prompt = f"""Imam više dokumenata, svaki označen kao DOKUMENT: [ime fajla].
Na osnovu pitanja koje ti postavljam, analiziraj koji dokument je najrelevantniji 
i odgovori na srpskom jeziku, obraćajući se studentu. Objasni jasno i jednostavno.Samo ispisi odgovor , ne moras navoditi u kom dokumentu si pronasao odgovor

{context}

Pitanje: {question}
"""
    response = model.generate_content(prompt)
    return response.text
