---
layout: default
---

# Fundamento: BOW, n-gramas y TF-IDF
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-03](../../../sesiones/sesion-03.md)

*(Alineado con la teoría de la Semana 3: [S03-NLP.tex](../teoria/S03-NLP.tex).)*

---

## 1. Bag of Words (BOW)

Cada documento = vector de frecuencias sobre vocabulario; **pierde orden**; sparse de alta dimensión.

---

## 2. N-gramas

Capturan orden local (bigramas, trigramas) a costa de **explosión** del vocabulario.

---

## 3. TF-IDF

\[
\text{tfidf}(t,d)=\text{tf}(t,d)\times \log\frac{N}{\text{df}(t)}
\]

Downweight de términos muy frecuentes en el corpus.

---

## 4. sklearn

`CountVectorizer`, `TfidfVectorizer`; parámetros `ngram_range`, `min_df`, `max_df`.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S03-NLP.tex](../teoria/S03-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
