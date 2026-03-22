---
layout: default
---

# Fundamento: Seq2Seq, encoder–decoder y atención
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-08](../../../sesiones/sesion-08.md)

*(Alineado con la teoría de la Semana 8: [S08-NLP.tex](../teoria/S08-NLP.tex).)*

---

## 1. Encoder–decoder

El encoder resume la fuente en un vector o secuencia de estados; el decoder genera la salida paso a paso (MT, resumen).

---

## 2. Teacher forcing

Durante entrenamiento se alimenta el decoder con tokens gold; en inferencia se usa salida previa (exposure bias).

---

## 3. Atención

Pesos \(\alpha_{ij}\) relacionan posición de salida \(i\) con posiciones de entrada \(j\); mitiga cuello de botella del vector único.

---

## 4. Beam search

Explora varias hipótesis de decodificación frente a greedy.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S08-NLP.tex](../teoria/S08-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
