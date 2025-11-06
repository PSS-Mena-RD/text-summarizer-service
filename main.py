from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import google.generativeai as genai
from pydantic import BaseModel
import json
import os

class TextIn(BaseModel):
    TextIn: str  # must match the JSON field name sent in the request

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
    content=input.TextIn
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"I will give you a text written in either Arabic, English, or a mix of both."
                                      f"Summarize the document in its most used language in no more than 250 words."
                                     "Return ONLY valid JSON with one key 'Text_Summary' and its value being the summary. "
        f"Here is the text:\n{content}")
    try:
        summary_json = json.loads(response.text)
    except json.JSONDecodeError:
        # If it’s not valid JSON, wrap it manually
        summary_json = {"Text_Summary": response.text.strip()}

    return JSONResponse(summary_json)
    return JSONResponse({"Text_Summary": summary})
@app.get("/")
def read_root():
    return {"message": "Service is running!"}