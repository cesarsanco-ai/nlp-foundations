---
layout: default
---

# Fundamento: redes neuronales para NLP y embeddings entrenables
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-06](../../../sesiones/sesion-06.md)

*(Alineado con la teoría de la Semana 6: [S06-NLP.tex](../teoria/S06-NLP.tex).)*

---

## 1. Embedding layer

Matriz \(E\in\mathbb{R}^{|V|\times d}\); índice de token → vector denso **aprendible**.

---

## 2. MLP / CNN sobre texto

Convoluciones 1D capturan n-gramas locales; pooling global → vector de documento.

---

## 3. Entrenamiento

Pérdida según tarea (cross-entropy); backprop a través de la capa de embedding.

---

## 4. vs embeddings fijos

Entrenar embeddings adapta el espacio a la tarea; riesgo de **overfitting** si datos son pocos.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S06-NLP.tex](../teoria/S06-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
