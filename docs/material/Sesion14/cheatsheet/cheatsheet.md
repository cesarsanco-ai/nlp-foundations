---
layout: default
---

# Cheatsheet: Despliegue NLP (MLOps)
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-14](../../../sesiones/sesion-14.md)

---

## Checklist de producción

| Área | Pregunta |
| :--- | :--- |
| **SLA** | ¿p99 latencia máxima? |
| **Coste** | ¿GPU vs CPU cuantizado? |
| **Seguridad** | ¿Datos sensibles en prompts? |
| **Rollback** | ¿Versión anterior lista? |

---

## vLLM / TGI (idea)

Servidores optimizados para **throughput** de LLM con KV-cache y batching continuo.

---

## Teoría

* [S14-NLP.tex](../teoria/S14-NLP.tex)

---

## Puntos críticos

* **Compatibilidad** tokenizer entre train y serve.
* Monitorear **tokens/s** y longitud de contexto real (no solo QPS).

> *“Un modelo en producción es un sistema: datos + modelo + infra + personas.”*
