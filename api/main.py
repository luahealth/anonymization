"""Basic post api to redact text"""
from fastapi import FastAPI
from pydantic import BaseModel
from anonymisation import main_ano
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Lua Health Anonymizer API",
    description="This is a self hosted API that allows clients to translate and anonymize messages. Currently the API handles English, Spanish and Tagalog.",
    docs_url=None,
    version='0.1.0',
    redoc_url="/docs",
    contact={
        "name": "Lua Health",
        "email": "info@luahealth.io",
    },
    license_info={
        "name": "Custom license",
        "url": "https://github.com/passive-prediction/anonymization#license",
    },)


thesaurus_path = "../thesaurus.txt"


class Message(BaseModel):
    text: str


@app.post("/redact/")
async def redact(message: Message):
    """
    Primary endpoint. Accepts a string and returns the same string translated and redacted.
    """
    text = (main_ano(message.text,thesaurus_path)
    return JSONResponse(content={'message':text})
