---
layout: default
---

# Fundamento: RAG, recuperación y bases vectoriales
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-12](../../../sesiones/sesion-12.md)

*(Alineado con la teoría de la Semana 12: [S12-NLP.tex](../teoria/S12-NLP.tex).)*

---

## 1. Pipeline RAG

Indexar documentos (chunks) → embedding → almacenamiento vectorial → recuperar top-k → condicionar al LLM.

---

## 2. Chunking

Tamaño, solapamiento y metadatos (fuente, fecha) afectan recall y trazabilidad.

---

## 3. Híbrido

BM25 + vectores (**hybrid search**) mejora cuando hay coincidencia léxica exacta.

---

## 4. Evaluación

Faithfulness, citation correctness, **answer relevance**; datasets sintéticos para ablation.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S12-NLP.tex](../teoria/S12-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
