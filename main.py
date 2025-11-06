from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os
app = FastAPI()

'''

@app.post("/summarize")
async def summarize(file: UploadFile):
    """
    Receives a text document and returns a summary.
    """
    content = await file.read()
    text = content.decode("utf-8")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"I will give you a document written in either Arabic, English, or a mix of both . Summarize the document in its most used language in no more than 250 words:\n{text}")
    summary = response.text
    return JSONResponse({"summary": summary})
'''
@app.post("/summarize")
async def summarize(input: TextIn):
    """
    Receives a text document and returns a summary.
    """
    #content = await file.read()
    #text = content.decode("utf-8")
    content=input.text
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"I will give you a text written in either Arabic, English, or a mix of both . Summarize the document in its most used language in no more than 250 words. Provide the summary as in JSON with the field Text_Summary: \n{text}")
    summary = response.text
    return JSONResponse({"summary": summary})
@app.get("/")
def read_root():
    return {"message": "Service is running!"}