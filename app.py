from fastapi import FastAPI, Request
from pydantic import BaseModel

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# =========================================
# Initialize FastAPI app
# =========================================

app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)


# =========================================
# Load Model & Tokenizer
# =========================================

model = T5ForConditionalGeneration.from_pretrained(
    "./saved_summary_model"
)

tokenizer = T5Tokenizer.from_pretrained(
    "./saved_summary_model"
)


# =========================================
# Device
# =========================================

if torch.backends.mps.is_available():
    device = torch.device("mps")

elif torch.cuda.is_available():
    device = torch.device("cuda")

else:
    device = torch.device("cpu")


model.to(device)

model.eval()


# =========================================
# Templates & Static Files
# =========================================

templates = Jinja2Templates(directory=".")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================
# Request Schema
# =========================================

class DialogueInput(BaseModel):
    dialogue: str


# =========================================
# Data Cleaning
# =========================================

def clean_data(text):

    text = re.sub(r"\r\n", " ", text)

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"<.*?>", " ", text)

    text = text.strip()

    text = text.lower()

    return text


# =========================================
# Summarization Function
# =========================================

def summarize_dialogue(dialogue: str) -> str:

    # Cleaning
    dialogue = clean_data(dialogue)

    # Tokenization
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # Generate summary
    with torch.no_grad():

        targets = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    # Token IDs → Text
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary


# =========================================
# API ENDPOINTS
# =========================================

@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):

    summary = summarize_dialogue(
        dialogue_input.dialogue
    )

    return {
        "summary": summary
    }


# =========================================
# Home Page
# =========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
