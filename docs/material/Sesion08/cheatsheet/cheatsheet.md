---
layout: default
---

# Cheatsheet: Seq2Seq y atención
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-08](../../../sesiones/sesion-08.md)

---

## Atención (idea)

\[
\text{context}(i)=\sum_j \alpha_{ij}\,h_j^{\text{enc}}
\]

Softmax sobre scores \(e_{ij}\) (Bahdanau / additive o dot-product).

---

## Decodificación

| Método | Trade-off |
| :--- | :--- |
| Greedy | Rápido, subóptimo |
| Beam | Mejor calidad, más coste |

---

## Teoría

* [S08-NLP.tex](../teoria/S08-NLP.tex)

---

## Puntos críticos

* **Long inputs** sin atención: información se pierde en el vector de contexto.
* Métricas MT: **BLEU** (n-gram overlap); complementar con evaluación humana.

> *“La atención es alineación aprendida entre fuente y destino.”*
