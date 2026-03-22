---
layout: default
---

# Fundamento: preprocesamiento — tokenización, normalización y regex
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-02](../../../sesiones/sesion-02.md)

*(Alineado con la teoría de la Semana 2: [S02-NLP.tex](../teoria/S02-NLP.tex).)*

---

## 1. Pipeline típico

Texto crudo → normalización (minúsculas, acentos según política) → **tokenización** → **stemming/lematización** → (opcional) stopwords.

---

## 2. Tokenización

Word-level, subword (BPE, SentencePiece); equilibrio entre vocabulario y OOV.

---

## 3. Regex

Patrones para extracción de fechas, menciones, limpieza de ruido HTML; cuidado con **greedy** vs **lazy**.

---

## 4. Lematización vs stemming

Lematización usa análisis morfológico (más precisa); stemming heurístico (más rápido).

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S02-NLP.tex](../teoria/S02-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
