---
layout: default
---

# Cheatsheet: Word2Vec y GloVe
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-04](../../../sesiones/sesion-04.md)

---

## Comparativa rápida

| Método | Entrenamiento |
| :--- | :--- |
| **Word2Vec** | Ventanas locales (SGNS/CBOW) |
| **GloVe** | Matriz de coocurrencias global |

---

## Analogías (idea)

\[
\vec(\text{rey}) - \vec(\text{hombre}) + \vec(\text{mujer}) \approx \vec(\text{reina})
\]

---

## gensim (esqueleto)

```python
from gensim.models import Word2Vec
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, workers=4)
```

---

## Teoría

* [S04-NLP.tex](../teoria/S04-NLP.tex)

---

## Puntos críticos

* OOV: palabras fuera del vocabulario de entrenamiento.
* Embeddings estáticos: una sola representación por palabra (ambigüedad).

> *“El embedding es la feature engineering del deep NLP clásico.”*
