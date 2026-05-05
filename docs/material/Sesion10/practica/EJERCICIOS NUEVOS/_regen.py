import json
from pathlib import Path

cells = []


def md(s):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in s.strip().split("\n")]})


def code(s):
    cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in s.strip().split("\n")],
        }
    )


md(
    """# Ejemplos: `pipeline` y modelos `Auto*` (Hugging Face Transformers)

**Sesión 10 · NLP** — Ocho ejemplos mínimos (el doble del bloque “3 pipeline + 1 pro” del guión), listos para **Google Colab** o Jupyter local.

**Contenido:** sentimiento (inglés y multilingüe), generación de texto (greedy y muestreo), traducción y resumen con **seq2seq + `generate`**, y dos variantes “pro” con `AutoTokenizer` + `AutoModel*` explícitos.

**Nota Colab:** la primera celda de código instala dependencias si faltan; la primera ejecución puede tardar por la descarga de modelos desde el Hub.

**Transformers 5.x:** en versiones recientes, el `pipeline` ya no registra por defecto las tareas `translation` y `summarization` (sí siguen existiendo modelos seq2seq). Los ejemplos 5 y 6 usan el mismo patrón que antes aplicaba el pipeline por dentro: tokenizar → `model.generate` → decodificar."""
)

md(
    """## 0. Entorno (instalación + comprobación)

En Colab puedes usar en su lugar una celda con `!pip install -q transformers torch sentencepiece`.

`sentencepiece` ayuda a algunos modelos de traducción/resumen; si `pip` no lo pide, no pasa nada."""
)

code(
    """import importlib.util
import subprocess
import sys


def _ensure(pkg: str) -> None:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])


_ensure("torch")
_ensure("transformers")
_ensure("sentencepiece")

import torch
import transformers

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("transformers:", transformers.__version__)
print("torch:", torch.__version__)
print("device:", device)"""
)

md(
    """## 1. Sintaxis básica (`pipeline`)

```python
from transformers import pipeline
nlp = pipeline("task")  # o pipeline("task", model="usuario/modelo")
resultado = nlp("Tu texto aquí")
```

**Tareas `pipeline` habituales:** `sentiment-analysis`, `text-generation`, … (según tu versión de `transformers`).

Para **traducción / resumen** con modelos Marian o BART, en este notebook usamos **seq2seq + `generate`** (ejemplos 5–6), equivalente a lo que hacía el `pipeline` en versiones anteriores.

---

### Ejemplo 1 — Análisis de sentimientos (modelo por defecto en inglés)

Equivalente al ejemplo del aula: el modelo por defecto suele ser SST-2 en inglés (`distilbert-base-uncased-finetuned-sst-2-english`)."""
)

code(
    """from transformers import pipeline

classifier = pipeline("sentiment-analysis")

resultado = classifier("Me encanta aprender inteligencia artificial")
print(resultado)"""
)

md(
    """### Ejemplo 2 — Sentimiento en español (modelo multilingüe explícito)

Misma tarea `sentiment-analysis`, pero fijando un modelo que admite varios idiomas (útil si el texto no está en inglés)."""
)

code(
    """from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
)

resultado = classifier("Este curso de NLP está muy bien explicado")
print(resultado)"""
)

md(
    """### Ejemplo 3 — Generación de texto (estilo GPT, greedy)

`max_new_tokens` limita cuántos tokens nuevos se generan."""
)

code(
    """from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

resultado = generator(
    "La inteligencia artificial es",
    max_new_tokens=20,
    pad_token_id=generator.tokenizer.eos_token_id,
)
print(resultado[0]["generated_text"])"""
)

md(
    """### Ejemplo 4 — Generación con muestreo (`do_sample=True`)

Misma tarea, pero la salida cambia en cada ejecución (más “creativo”)."""
)

code(
    """from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

resultado = generator(
    "Machine learning can",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.9,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)
print(resultado[0]["generated_text"])"""
)

md(
    """### Ejemplo 5 — Traducción inglés → español (Marian + `generate`)

Modelo `Helsinki-NLP/opus-mt-en-es`. Patrón seq2seq: tokenizar, `generate`, decodificar."""
)

code(
    """import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

texto = "Machine learning is amazing"
inputs = tokenizer(texto, return_tensors="pt", truncation=True, max_length=512).to(device)

with torch.no_grad():
    ids = model.generate(**inputs, max_new_tokens=128)

print(tokenizer.decode(ids[0], skip_special_tokens=True))"""
)

md(
    """### Ejemplo 6 — Resumen (DistilBART + `generate`)

Necesita un párrafo largo de entrada."""
)

code(
    """import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
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

print(tokenizer.decode(summary_ids[0], skip_special_tokens=True))"""
)

md(
    """## 2. Versión un poco más “pro” (modelo + tokenizer explícitos)

---

### Ejemplo 7 — Clasificación de secuencias con `AutoTokenizer` + `AutoModelForSequenceClassification`

Igual que en el guión: DistilBERT SST-2, pero cargando tokenizer y modelo a mano y pasándolos al `pipeline`."""
)

code(
    """from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

modelo = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSequenceClassification.from_pretrained(modelo)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

print(classifier("This is awesome"))"""
)

md(
    """### Ejemplo 8 — Traducción “pro”: beams + control de longitud

Mismo modelo Marian que el ejemplo 5, pero fijando `num_beams` y límites de generación (suele dar traducciones algo más estables)."""
)

code(
    """import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
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

print(tokenizer.decode(ids[0], skip_special_tokens=True))"""
)

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

out = Path(__file__).parent / "ejemplos.ipynb"
out.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("Wrote", out)
