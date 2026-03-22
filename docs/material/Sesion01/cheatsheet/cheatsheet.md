---
layout: default
---

# Cheatsheet: Fundamentos de NLP
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-01](../../../sesiones/sesion-01.md)

---

## Tareas comunes

| Tarea | Salida |
| :--- | :--- |
| Clasificación | Etiqueta |
| NER | Entidades + tipos |
| MT / resumen | Texto |
| Embeddings | Vector por token o doc |

---

## spaCy (inicio rápido)

```python
import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("El gato duerme.")
[t.text for t in doc]
```

---

## Teoría

* [S01-NLP.tex](../teoria/S01-NLP.tex)

---

## Puntos críticos

* **Tokenización** depende del idioma y del modelo.
* Evaluar con datos **representativos** del despliegue.

> *“NLP = señal discreta + ambigüedad; el contexto lo resuelve todo.”*
