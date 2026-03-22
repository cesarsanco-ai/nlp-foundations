---
layout: default
---

# Fundamento: RNN, LSTM y GRU
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-07](../../../sesiones/sesion-07.md)

*(Alineado con la teoría de la Semana 7: [S07-NLP.tex](../teoria/S07-NLP.tex).)*

---

## 1. RNN

Estado oculto \(h_t = \tanh(W_{hh}h_{t-1}+W_{xh}x_t+b)\); memoria recurrente pero **gradientes** pueden explotar/desvanecer.

---

## 2. LSTM

Celdas **input/forget/output** y estado de celda \(c_t\) para trayectorias largas.

---

## 3. GRU

Variante con menos puertas; a menudo comparable con menos parámetros.

---

## 4. Bidireccionalidad

`BiLSTM` concatena pasadas forward/backward para etiquetado de secuencias.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S07-NLP.tex](../teoria/S07-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
