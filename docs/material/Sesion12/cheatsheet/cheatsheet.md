---
layout: default
---

# Cheatsheet: RAG y vector DB
**Autor:** Carlos César Sánchez Coronel  

[⬅️ Volver a la Sesión-12](../../../sesiones/sesion-12.md)

---

## Pasos

1. `chunk` documentos  
2. `embed` con modelo alineado a consulta  
3. `upsert` en índice (p. ej. FAISS, Milvus, Pinecone)  
4. `retrieve` + prompt  

---

## Prompt mínimo

```
Contexto:
{chunks}

Pregunta: {q}
Responde solo con base en el contexto.
```

---

## Teoría

* [S12-NLP.tex](../teoria/S12-NLP.tex)

---

## Puntos críticos

* **Duplicados** en el índice inflan contexto sin información nueva.
* Re-ranking (cross-encoder) tras ANN mejora precisión@k.

> *“RAG = recuperación barata + generación cara, acotada.”*
