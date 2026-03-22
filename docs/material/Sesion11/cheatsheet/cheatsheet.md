---
layout: default
---

# Cheatsheet: NER, QA y summarization
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-11](../../../sesiones/sesion-11.md)

---

## Esquema BIO

| Etiqueta | Significado |
| :--- | :--- |
| B-PER | Inicio persona |
| I-PER | Continuación |
| O | Fuera de entidad |

---

## Métricas

| Tarea | Métrica frecuente |
| :--- | :--- |
| NER | F1 por tipo / micro F1 |
| Resumen | ROUGE-1/2/L |

---

## Teoría

* [S11-NLP.tex](../teoria/S11-NLP.tex)

---

## Puntos críticos

* **Nested NER** requiere formalismos más ricos que BIO plano.
* QA: **contexto** demasiado largo → truncar o retriever.

> *“NER es sequence labeling; el CRF alinea transiciones válidas.”*
