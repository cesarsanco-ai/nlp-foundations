---
layout: default
---

# Cheatsheet: Fine-tuning BERT / GPT
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-10](../../../sesiones/sesion-10.md)

---

## Hugging Face Trainer (idea)

```python
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
args = TrainingArguments(output_dir="out", learning_rate=2e-5, per_device_train_batch_size=16)
```

---

## Hiperparámetros

| Parámetro | Típico |
| :--- | :--- |
| LR | \(2\text{e-}5\) – \(5\text{e-}5\) para BERT |
| Épocas | 2–5 (sobreajuste rápido) |
| Max length | Según GPU |

---

## Teoría

* [S10-NLP.tex](../teoria/S10-NLP.tex)

---

## Puntos críticos

* **Catastrophic forgetting** si LR demasiado alto o pocos datos.
* Usar **weighted loss** con clases desbalanceadas.

> *“Fine-tuning es transfer learning: el pretrain ya trae sintaxis y mundo.”*
