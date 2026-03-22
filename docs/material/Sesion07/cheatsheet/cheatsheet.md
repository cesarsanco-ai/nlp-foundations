---
layout: default
---

# Cheatsheet: RNN, LSTM, GRU
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-07](../../../sesiones/sesion-07.md)

---

## Ecuación RNN (esquema)

\(h_t = \tanh(W_{hh}h_{t-1} + W_{xh}x_t + b)\)

---

## PyTorch

```python
import torch.nn as nn
rnn = nn.LSTM(input_size=dim, hidden_size=hid, num_layers=1, batch_first=True, bidirectional=True)
```

---

## Cuándo usar

| Celda | Nota |
| :--- | :--- |
| **LSTM/GRU** | Secuencias largas |
| **Vanilla RNN** | Raramente solo; didáctico |

---

## Teoría

* [S07-NLP.tex](../teoria/S07-NLP.tex)

---

## Puntos críticos

* **pack_padded_sequence** para eficiencia con longitudes variables.
* Transformers suelen superar a RNN en paralelización y dependencias largas.

> *“LSTM es un camino de gradiente más estable que RNN puro.”*
