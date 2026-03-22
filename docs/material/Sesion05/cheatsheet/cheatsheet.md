---
layout: default
---

# Cheatsheet: Naive Bayes y SVM
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-05](../../../sesiones/sesion-05.md)

---

## sklearn

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
    ("clf", LinearSVC()),
])
```

---

## Cuándo usar qué

| Modelo | Ventaja |
| :--- | :--- |
| **MultinomialNB** | Muy rápido, bueno con conteos |
| **LinearSVC** | Suelde bien con TF-IDF sparse |

---

## Teoría

* [S05-NLP.tex](../teoria/S05-NLP.tex)

---

## Puntos críticos

* **Calibración** de probabilidades: NB sí; SVM lineal requiere `CalibratedClassifierCV` si necesitas `predict_proba` fiable.
* Regularización `C` en SVM y límites de memoria en features gigantes.

> *“No subestimes TF-IDF + SVM frente a BERT en datasets chicos.”*
