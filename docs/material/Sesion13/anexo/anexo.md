---
layout: default
---

# Fundamento: prompt engineering, LoRA y cuantización
#### Autor: Carlos César Sánchez Coronel

[⬅️ Volver a la Sesión-13](../../../sesiones/sesion-13.md)

*(Alineado con la teoría de la Semana 13: [S13-NLP.tex](../teoria/S13-NLP.tex).)*

---

## 1. Prompting

Instrucciones claras, ejemplos few-shot, formato de salida (JSON, listas); **chain-of-thought** cuando el razonamiento explícito ayuda.

---

## 2. LoRA / adaptadores

Actualizaciones de **bajo rango** sobre pesos de atención: entrenar solo \(\Delta W \approx BA\) con \(r\ll d\).

---

## 3. Cuantización

INT8/INT4 (GGML, bitsandbytes) para inferencia en GPU/CPU limitada; **QLoRA** entrena LoRA sobre base cuantizada.

---

## 4. Coste y latencia

Trade-off precisión vs tamaño de modelo y throughput.

---

## 5. Enlaces directos

* **Teoría LaTeX:** [S13-NLP.tex](../teoria/S13-NLP.tex)
* **CheatSheet:** [cheatsheet.md](../cheatsheet/cheatsheet.md)
