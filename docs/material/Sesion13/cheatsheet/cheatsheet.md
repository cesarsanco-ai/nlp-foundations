---
layout: default
---

# Cheatsheet: Prompts, LoRA, cuantización
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-13](../../../sesiones/sesion-13.md)

---

## LoRA (idea)

W' = W + BA, \(B\in\mathbb{R}^{d\times r}, A\in\mathbb{R}^{r\times k}\), \(r\ll d\)

---

## bitsandbytes (HF)

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", quantization_config=bnb)
```

---

## Prompt checklist

| Elemento | Pregunta |
| :--- | :--- |
| Rol | ¿Quién es el modelo? |
| Formato | ¿JSON? ¿tabla? |
| Restricciones | ¿Longitud? ¿idioma? |

---

## Teoría

* [S13-NLP.tex](../teoria/S13-NLP.tex)

---

## Puntos críticos

* **Temperature** alta → creatividad; baja → determinismo.
* Evaluar **seguridad** (jailbreaks) al cambiar prompts.

> *“LoRA reduce GPU necesaria para adaptar sin full fine-tune.”*
