---
layout: default
---

# Fundamento: Naive Bayes y SVM para texto
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-05](../../../sesiones/sesion-05.md)

*(Alineado con la teoría de la Semana 5: [S05-NLP.tex](../teoria/S05-NLP.tex).)*

---

## 1. Naive Bayes

Modelo generativo con supuesto de **independencia condicional** entre features dada la clase; eficiente en alta dimensión sparse (TF-IDF).

---

## 2. Multinomial vs Bernoulli

Conteos de términos vs presencia/ausencia; elegir según representación.

---

## 3. SVM

Hiperplano de **máximo margen**; kernel lineal muy usado con TF-IDF; kernels no lineales si features lo justifican.

---

## 4. Baseline

Antes de redes profundas, NB/SVM + TF-IDF suelen ser **baselines fuertes** en datasets pequeños/medianos.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S05-NLP.tex](../teoria/S05-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
