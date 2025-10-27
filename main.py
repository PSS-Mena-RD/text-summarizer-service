from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os
app = FastAPI()

@app.post("/summarize")
async def summarize(file: UploadFile, api_key: str = Form(...)):
    """
    Receives a text document and returns a summary.
    """
    content = await file.read()
    text = content.decode("utf-8")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"Summarize the following Arabic text in no more than 250 words:\n{text}")
    summary = response.text
    return JSONResponse({"summary": summary})