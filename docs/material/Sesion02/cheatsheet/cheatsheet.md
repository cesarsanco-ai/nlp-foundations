---
layout: default
---

# Cheatsheet: Preprocesamiento
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-02](../../../sesiones/sesion-02.md)

---

## Decisiones

| Paso | Opción típica |
| :--- | :--- |
| Minúsculas | Clasificación general; cuidado con siglas |
| Stopwords | A menudo se eliminan en BOW; en Transformers no |
| Tokenizer | Debe coincidir con el modelo pre-entrenado |

---

## Regex (Python)

```python
import re
re.sub(r"\s+", " ", text).strip()
```

---

## Teoría

* [S02-NLP.tex](../teoria/S02-NLP.tex)

---

## Puntos críticos

* **Reproducibilidad:** fija el mismo preprocesamiento en train y serve.
* Subword tokenizers **no** son reversibles token a token de forma trivial.

> *“El mejor preprocesamiento es el que el modelo downstream espera.”*
