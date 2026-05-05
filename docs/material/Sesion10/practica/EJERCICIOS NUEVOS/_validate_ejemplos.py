"""Smoke test for ejemplos.ipynb code (mirrors each code cell)."""
import importlib.util
import subprocess
import sys


def _ensure(pkg: str) -> None:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])


_ensure("torch")
_ensure("transformers")
_ensure("sentencepiece")

import torch
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
)

# 1
classifier = pipeline("sentiment-analysis")
assert classifier("Me encanta aprender inteligencia artificial")[0]["score"] > 0

# 2
classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
)
assert classifier("Este curso de NLP está muy bien explicado")

# 3
generator = pipeline("text-generation", model="gpt2")
resultado = generator(
    "La inteligencia artificial es",
    max_new_tokens=20,
    pad_token_id=generator.tokenizer.eos_token_id,
)
assert "generated_text" in resultado[0]

# 4
generator = pipeline("text-generation", model="gpt2")
resultado = generator(
    "Machine learning can",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.9,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)
assert "generated_text" in resultado[0]

# 5
model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
texto = "Machine learning is amazing"
inputs = tokenizer(texto, return_tensors="pt", truncation=True, max_length=512).to(device)
with torch.no_grad():
    ids = model.generate(**inputs, max_new_tokens=128)
out = tokenizer.decode(ids[0], skip_special_tokens=True)
assert len(out) > 0

# 6
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.to(device)
texto_largo = (
    "The Hugging Face transformers library provides pretrained models for natural language "
    "processing tasks such as classification, generation, translation, and summarization. "
    "Pipelines wrap a tokenizer and a model to return ready-to-use predictions with a few lines of code. "
    "Users can swap models by changing the model name while keeping the same task API."
)
inputs = tokenizer(texto_largo, return_tensors="pt", truncation=True, max_length=1024).to(device)
with torch.no_grad():
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=60,
        min_length=20,
        num_beams=4,
        early_stopping=True,
    )
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
assert len(summary) > 0

# 7
modelo = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSequenceClassification.from_pretrained(modelo)
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
assert classifier("This is awesome")

# 8
model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.to(device)
texto = "Machine learning is amazing"
inputs = tokenizer(texto, return_tensors="pt", truncation=True, max_length=512).to(device)
with torch.no_grad():
    ids = model.generate(
        **inputs,
        max_new_tokens=128,
        num_beams=4,
        length_penalty=1.0,
        early_stopping=True,
    )
out2 = tokenizer.decode(ids[0], skip_special_tokens=True)
assert len(out2) > 0

print("OK: all 8 ejemplo blocks ran successfully")
