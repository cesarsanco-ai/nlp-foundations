---
layout: default
---

# Cheatsheet: Redes neuronales y embeddings
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-06](../../../sesiones/sesion-06.md)

---

## PyTorch (embedding + media)

```python
import torch.nn as nn
emb = nn.Embedding(vocab_size, dim)
# x: [batch, seq] índices → emb(x): [batch, seq, dim]
```

---

## CNN 1D (idea)

`nn.Conv1d` sobre secuencia de embeddings; `ReLU` + `AdaptiveMaxPool1d` → vector fijo.

---

## Teoría

* [S06-NLP.tex](../teoria/S06-NLP.tex)

---

## Puntos críticos

* **Padding** y máscaras para no promediar tokens `<pad>`.
* Inicializar embeddings con pre-entrenados (GloVe) y **congelar** o **fine-tune** parcialmente.

> *“El embedding es la primera capa que traduce tokens a geometría.”*
