---
layout: default
---

# Fundamento: modelos pre-entrenados, BERT y fine-tuning
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-10](../../../sesiones/sesion-10.md)

*(Alineado con la teoría de la Semana 10: [S10-NLP.tex](../teoria/S10-NLP.tex).)*

---

## 1. Pre-entrenamiento

Objetivos **MLM** (BERT), **causal LM** (GPT); aprenden representaciones universales del lenguaje.

---

## 2. Fine-tuning

Añadir cabeza de clasificación / token classification; entrenar con LR bajo sobre datos de dominio.

---

## 3. BERT vs GPT

Encoder bidireccional (representación de frase) vs decoder autoregresivo (generación).

---

## 4. Práctica

Congelar capas inferiores, **gradient accumulation** si GPU pequeña, mixed precision.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S10-NLP.tex](../teoria/S10-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
