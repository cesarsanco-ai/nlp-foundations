---
layout: default
---

# Cheatsheet: BOW, TF-IDF y n-gramas
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-03](../../../sesiones/sesion-03.md)

---

## Fórmulas

| Concepto | Idea |
| :--- | :--- |
| TF | Frecuencia del término en el doc |
| IDF | Penaliza términos demasiado comunes |
| TF-IDF | Producto (variantes con normalización) |

---

## sklearn

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer(ngram_range=(1,2), min_df=2)
X = vec.fit_transform(corpus)
```

---

## Teoría

* [S03-NLP.tex](../teoria/S03-NLP.tex)

---

## Puntos críticos

* **Sinónimos** no resueltos: “coche” vs “auto”.
* `min_df` / `max_df` controlan ruido y memoria.

> *“TF-IDF sigue siendo baseline fuerte en texto corto tabular.”*
