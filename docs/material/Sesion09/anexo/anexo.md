---
layout: default
---

# Fundamento: Transformers, self-attention y codificación posicional
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-09](../../../sesiones/sesion-09.md)

*(Alineado con la teoría de la Semana 9: [S09-NLP.tex](../teoria/S09-NLP.tex).)*

---

## 1. Self-attention

Cada token consulta a todos: \(Q,K,V\) lineales de la entrada; \(\text{softmax}(QK^\top/\sqrt{d_k})V\).

---

## 2. Multi-head

Varias cabezas en paralelo capturan relaciones distintas; concatenación y proyección final.

---

## 3. Positional encoding

Seno/coseno o embeddings aprendidos; el modelo no tiene recurrencia, así que el orden se inyecta explícitamente.

---

## 4. Encoder vs decoder

Encoder: self-attention bidireccional; decoder: **máscara causal** para autoregresión.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S09-NLP.tex](../teoria/S09-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
