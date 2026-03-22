---
layout: default
---

# Cheatsheet: Transformers
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-09](../../../sesiones/sesion-09.md)

---

## Scaled dot-product attention

\[
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

---

## Bloque transformer (encoder)

Self-attention → Add&Norm → FFN → Add&Norm

---

## Hugging Face (esqueleto)

```python
from transformers import AutoModel
model = AutoModel.from_pretrained("bert-base-uncased")
```

---

## Teoría

* [S09-NLP.tex](../teoria/S09-NLP.tex)

---

## Puntos críticos

* Complejidad \(O(n^2)\) en longitud de secuencia.
* **Causal mask** obligatoria en LM / decoder.

> *“Self-attention = grafo completo entre tokens con pesos aprendidos.”*
