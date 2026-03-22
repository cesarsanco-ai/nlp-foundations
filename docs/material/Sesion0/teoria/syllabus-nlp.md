# Sílabo del Curso

# **PROCESAMIENTO DE LENGUAJE NATURAL (NLP)**
## *para Inteligencia Artificial*

**De los fundamentos lingüísticos a los modelos generativos**

*Por*

**Carlos César Sánchez Coronel**

2026


---

## Presentación del Curso

Este curso ha sido diseñado para futuros ingenieros en inteligencia artificial que deseen dominar el Procesamiento de Lenguaje Natural (NLP) desde una perspectiva práctica y orientada a la industria. A lo largo de 14 semanas, exploraremos desde las técnicas clásicas de preprocesamiento hasta la arquitectura de transformers y los modelos generativos, con un enfoque en las preguntas y habilidades que se esperan en entrevistas técnicas.

Cada tema será abordado con teoría sólida, implementaciones en Python usando librerías estándar (NLTK, spaCy, Hugging Face, PyTorch) y ejemplos de casos reales como chatbots, análisis de sentimiento, sistemas de búsqueda semántica y asistentes virtuales. Al finalizar, el estudiante estará preparado para enfrentar desafíos de modelado de lenguaje y comprender el ciclo completo de un proyecto de NLP, desde la recolección de datos hasta el despliegue en producción.

**Estructura del curso (14 semanas):**
- ☐ Semanas 1-3: Fundamentos y preprocesamiento
- ☐ Semanas 4-6: Representación del lenguaje y modelos clásicos
- ☐ Semanas 7-9: Modelos de deep learning para secuencias
- ☐ Semanas 10-12: Transformers y modelos pre-entrenados
- ☐ Semanas 13-14: Aplicaciones avanzadas y despliegue

---

## Semana 1: Introducción a NLP y Fundamentos Lingüísticos

### Logro de la sesión
Comprender el alcance del NLP, sus aplicaciones en la industria y los conceptos lingüísticos básicos que subyacen al procesamiento del lenguaje.

#### Conceptos
- Definición de NLP: objetivos, desafíos y áreas de aplicación.
- Niveles del lenguaje: morfología, sintaxis, semántica, pragmática.
- Part-of-Speech (POS) tagging y parsing.
- Corpus y datasets anotados.
- Aplicaciones reales: chatbots, análisis de sentimiento, traducción automática, búsqueda semántica.

#### Aplicaciones en el mundo laboral y entrevistas
- Pregunta típica: "¿Qué es NLP y dónde se usa?" Se espera mencionar casos concretos como atención al cliente, detección de fraudes en textos financieros, análisis de redes sociales.
- Entender la diferencia entre sintaxis (estructura) y semántica (significado).

#### Python
- Introducción a NLTK y spaCy: carga de pipelines, exploración de corpora.
- Visualización de árboles de dependencia con spaCy.

---

## Semana 2: Preprocesamiento de Texto

### Logro de la sesión
Aplicar técnicas de limpieza y normalización de texto para preparar datos para modelos de NLP.

#### Conceptos
- Tokenización: palabras, oraciones, subpalabras (BPE, WordPiece, Unigram).
- Normalización: minúsculas, eliminación de caracteres especiales, manejo de URLs y emojis.
- Eliminación de stopwords.
- Stemming vs. Lemmatization: diferencias y cuándo usar cada una.
- Manejo de expresiones regulares (regex) para limpieza avanzada.
- Desafíos en NLP: Out-of-Vocabulary (OOV) words y cómo los métodos de subpalabras los resuelven.

#### Aplicaciones y entrevistas
- Pregunta clave: "¿Cuándo usar stemming y cuándo lematización?"
- Conocimiento de algoritmos de tokenización como BPE (usado en GPT) y WordPiece (usado en BERT).

#### Python
- Uso de NLTK y spaCy para tokenización, lematización y eliminación de stopwords.
- Práctica con regex para limpieza de texto ruidoso.
- Implementación simple de BPE con librerías como `tokenizers`.

---

## Semana 3: Representación del Texto: BOW, TF-IDF y N-gramas

### Logro de la sesión
Transformar texto en vectores numéricos utilizando técnicas clásicas de representación.

#### Conceptos
- Bag of Words (BOW): frecuencia de términos, limitaciones (pérdida de orden y semántica).
- N-gramas: capturar contexto local.
- TF-IDF (Term Frequency-Inverse Document Frequency): ponderación de términos según su importancia.
- Limitaciones de las representaciones dispersas (sparse representations).

#### Aplicaciones y entrevistas
- Pregunta frecuente: "Compara Bag of Words, TF-IDF y embeddings. ¿Cuándo usarías cada uno?"
- Saber que TF-IDF penaliza palabras muy comunes (como artículos) y resalta términos distintivos.

#### Python
- Implementación con `sklearn.feature_extraction.text.CountVectorizer` y `TfidfVectorizer`.
- Análisis de documentos con estas representaciones.

---

## Semana 4: Word Embeddings: Word2Vec y GloVe

### Logro de la sesión
Comprender el concepto de embeddings densos y entrenar/visualizar word embeddings.

#### Conceptos
- Limitaciones de las representaciones dispersas: maldición de la dimensionalidad, falta de semántica.
- Word2Vec: modelos Skip-gram y CBOW, entrenamiento con ventanas de contexto.
- GloVe (Global Vectors): factorización de matrices de co-ocurrencia.
- Propiedades de los embeddings: relaciones semánticas (rey - hombre + mujer ≈ reina).
- Embeddings contextuales vs. estáticos.

#### Aplicaciones y entrevistas
- Pregunta técnica: "Explica la diferencia entre Skip-gram y CBOW".
- Saber interpretar la analogía de embeddings en entrevistas.

#### Python
- Entrenar Word2Vec con `gensim` sobre un corpus pequeño.
- Visualizar embeddings con PCA/t-SNE y matplotlib.
- Cargar embeddings pre-entrenados de GloVe y explorar similitudes.

---

## Semana 5: Modelos Clásicos para NLP (Naive Bayes, SVM)

### Logro de la sesión
Aplicar algoritmos de machine learning clásicos a tareas de NLP como clasificación de texto.

#### Conceptos
- Naive Bayes para clasificación de texto: supuesto de independencia, cálculo de probabilidades.
- Support Vector Machines (SVM) con kernels lineales para textos.
- Ventajas y limitaciones de modelos clásicos frente a deep learning.

#### Aplicaciones y entrevistas
- Pregunta típica: "Menciona dos algoritmos clásicos para clasificación de textos".
- Saber que Naive Bayes es rápido y funciona bien con datos pequeños, pero asume independencia de características.

#### Python
- Implementación de clasificador Naive Bayes con `sklearn` sobre dataset de noticias (20 Newsgroups).
- Comparación con SVM lineal.
- Evaluación con métricas de clasificación (accuracy, F1-score).

---

## Semana 6: Redes Neuronales para NLP y Embeddings Entrenables

### Logro de la sesión
Construir redes neuronales simples para tareas de NLP usando PyTorch.

#### Conceptos
- De los embeddings estáticos a los embeddings entrenables.
- Capa de embedding en PyTorch.
- Redes feed-forward para clasificación de texto (promedio de embeddings + MLP).
- Función de pérdida: Cross-Entropy.
- Regularización en NLP: dropout, weight decay.

#### Aplicaciones y entrevistas
- Pregunta: "¿Cómo representarías una oración para ingresarla a una red neuronal?" (respuesta: promedio de embeddings o concatenación).
- Saber que los embeddings entrenables se ajustan a la tarea específica.

#### Python
- Implementación de un clasificador simple con embeddings entrenables en PyTorch.
- Entrenamiento sobre dataset de IMDb para análisis de sentimiento.
- Comparación con embeddings pre-entrenados estáticos.

---

## Semana 7: Redes Recurrentes (RNN, LSTM, GRU) para NLP

### Logro de la sesión
Modelar secuencias de texto utilizando redes recurrentes y entender sus limitaciones.

#### Conceptos
- RNN (Recurrent Neural Networks): cómo procesan secuencias, estado oculto.
- Problema del gradiente desvaneciente (vanishing gradient).
- LSTM (Long Short-Term Memory): celdas de memoria, puertas (input, forget, output).
- GRU (Gated Recurrent Unit): versión simplificada de LSTM.

#### Aplicaciones y entrevistas
- Pregunta avanzada: "Explica por qué LSTM funciona mejor que RNN vanilla para secuencias largas".
- Saber que LSTM fue el estado del arte antes de los transformers.

#### Python
- Implementación de LSTM para clasificación de sentimiento con PyTorch.
- Comparación de rendimiento entre RNN simple y LSTM.
- Uso de embeddings pre-entrenados con LSTM.

---

## Semana 8: Modelos Seq2Seq y Atención

### Logro de la sesión
Construir modelos de secuencia a secuencia (Seq2Seq) para tareas como traducción automática y summarization.

#### Conceptos
- Arquitectura Encoder-Decoder.
- Context vector fijo y su limitación.
- Mecanismo de atención: alineación entre palabras de entrada y salida.
- Tipos de atención: global vs. local.
- Métricas para traducción: BLEU (Bilingual Evaluation Understudy).

#### Aplicaciones y entrevistas
- Pregunta fundamental: "¿Cómo funciona el mecanismo de atención?"
- La atención es la base de los transformers; entenderla es clave.
- Saber que BLEU mide la similitud entre traducción automática y referencia.

#### Python
- Implementación de un modelo Seq2Seq con atención usando PyTorch.
- Entrenamiento para tarea de traducción simple (ej. inglés-español con dataset pequeño).
- Evaluación con BLEU usando `sacrebleu`.

---

## Semana 9: Transformers - Arquitectura y Atención Multi-Head

### Logro de la sesión
Comprender la arquitectura del transformer y su revolución en NLP.

#### Conceptos
- El paper "Attention is All You Need".
- Arquitectura del transformer: encoder, decoder, multi-head attention, positional encoding, feed-forward layers.
- Self-attention y atención cruzada (cross-attention).
- Ventajas sobre RNN: paralelización, captura de dependencias largas.

#### Aplicaciones y entrevistas
- Pregunta estrella: "Explica cómo funciona el transformer y qué problema resuelve".
- Saber qué es positional encoding y por qué es necesario.

#### Python
- Implementación de una capa de self-attention desde cero con PyTorch.
- Exploración de la librería Hugging Face Transformers.
- Uso de modelos pre-entrenados para inferencia.

---

## Semana 10: Modelos Pre-entrenados (BERT, GPT) y Fine-tuning

### Logro de la sesión
Utilizar y fine-tunar modelos pre-entrenados como BERT y GPT para tareas específicas.

#### Conceptos
- BERT (Bidirectional Encoder Representations from Transformers): entrenamiento con MLM (Masked Language Model) y NSP (Next Sentence Prediction).
- GPT (Generative Pre-trained Transformer): entrenamiento autorregresivo.
- Fine-tuning vs. feature-based approaches.
- Tokenizadores de subpalabras (WordPiece, BPE).
- Métricas para clasificación: accuracy, F1, AUC.

#### Aplicaciones y entrevistas
- Pregunta común: "¿Cuál es la diferencia entre BERT y GPT?"
- Saber cuándo usar fine-tuning completo y cuándo usar adaptadores (LoRA).

#### Python
- Fine-tuning de BERT para clasificación de textos usando Hugging Face.
- Uso de GPT para generación de texto.
- Implementación de early stopping y guardado de checkpoints.

---

## Semana 11: Tareas Avanzadas: NER, Question Answering, Summarization

### Logro de la sesión
Aplicar modelos pre-entrenados a tareas específicas de NLP como Named Entity Recognition (NER) y extracción de respuestas.

#### Conceptos
- Named Entity Recognition (NER): etiquetado de entidades (personas, organizaciones, lugares).
- Question Answering (QA): modelos extractivos (SQuAD) y generativos.
- Summarization: extractivo vs. abstractivo.
- Métricas de evaluación: F1 para NER, exact match para QA, ROUGE para summarization.

#### Aplicaciones y entrevistas
- Pregunta: "¿Qué métrica usarías para evaluar un sistema de NER?" (F1-score por entidad).
- Saber que ROUGE mide solapamiento de n-gramas entre resumen generado y referencia.

#### Python
- Fine-tuning de BERT para NER con Hugging Face.
- Uso de pipelines de Hugging Face para QA y summarization.
- Evaluación con métricas específicas.

---

## Semana 12: RAG (Retrieval-Augmented Generation) y Bases de Datos Vectoriales

### Logro de la sesión
Diseñar sistemas que combinan recuperación de información con generación de lenguaje (RAG).

#### Conceptos
- Limitaciones de los LLMs: conocimiento desactualizado, alucinaciones.
- RAG (Retrieval-Augmented Generation): recuperar información relevante de una base de conocimiento y pasarla al LLM como contexto.
- Embeddings para búsqueda semántica.
- Bases de datos vectoriales: FAISS, Pinecone, Weaviate.
- Evaluación de sistemas RAG: faithfulness, relevance.

#### Aplicaciones y entrevistas
- Pregunta clave: "¿Qué es RAG y cuándo lo usarías?"
- Saber que RAG reduce alucinaciones y permite usar conocimiento actualizado sin reentrenar.

#### Python
- Construcción de un pipeline RAG: cargar documentos, crear embeddings con Sentence Transformers, almacenar en FAISS, recuperar y generar con GPT.
- Implementación de un chatbot que responda sobre documentos propios.

---

## Semana 13: Prompt Engineering y Optimización de Modelos

### Logro de la sesión
Dominar técnicas de prompt engineering y métodos de optimización como LoRA y cuantización.

#### Conceptos
- Prompt engineering: zero-shot, few-shot, chain-of-thought.
- In-context learning.
- Fine-tuning eficiente: LoRA (Low-Rank Adaptation), adaptadores.
- Cuantización: reducción de precisión para inferencia más rápida (INT8, FP16).
- Exportación de modelos a ONNX.

#### Aplicaciones y entrevistas
- Pregunta avanzada: "¿Qué es LoRA y por qué es útil?"
- Saber que la cuantización reduce el tamaño del modelo y acelera inferencia a costa de pequeña pérdida de precisión.

#### Python
- Experimentación con prompts para GPT usando librerías como `openai` o modelos locales.
- Fine-tuning con LoRA usando `peft` y `transformers`.
- Cuantización con `torch.quantization` u ONNX.

---

## Semana 14: Despliegue de Modelos NLP (MLOps)

### Logro de la sesión
Llevar un modelo NLP a producción, crear APIs y monitorear su rendimiento.

#### Conceptos
- Separación entre entrenamiento e inferencia.
- Serialización de modelos: pickle, joblib, ONNX, TorchScript.
- Creación de APIs REST con Flask o FastAPI.
- Contenerización con Docker.
- Monitoreo de modelos en producción: data drift, concept drift, latencia, throughput.
- Versionamiento de modelos con DVC o Hugging Face Hub.

#### Aplicaciones y entrevistas
- Pregunta clave: "¿Cómo desplegarías un modelo NLP en producción?"
- Saber que se debe monitorear la deriva de datos y la latencia.

#### Python
- Creación de una API con FastAPI que carga un modelo fine-tuneado y recibe textos para clasificar.
- Dockerización de la aplicación.
- Pruebas de carga y monitoreo básico.

---

## Metodología y Evaluación

### Estrategias metodológicas
- **Clases síncronas:** Exposición conceptual con diapositivas, programación en vivo con Python utilizando cuadernos de Jupyter y Hugging Face.
- **Trabajo asíncrono:** Lectura de papers seminales ("Attention is All You Need"), ejercicios prácticos y proyectos semanales.
- **Aprendizaje activo:** Simulacros de entrevistas técnicas, discusión de casos reales, retos de código.
- **Recursos:** Plataforma virtual, Zoom, grabaciones, foros y repositorio GitHub.

### Materiales educativos
- Cuadernos de Jupyter con ejemplos y ejercicios.
- Acceso a modelos en Hugging Face y datasets.
- Bibliografía: Jurafsky & Martin (Speech and Language Processing), papers originales.
- Google Colab Pro para GPU.

### Evaluación

| **Ítem** | **Ponderación** |
|----------|-----------------|
| Evaluaciones continuas (EC) | 40% |
| Examen parcial (EP) - Semana 7 | 30% |
| Examen final (EF) - Semana 14 | 30% |
| **Promedio final (PF)** | PF = 0.4 × EC + 0.3 × EP + 0.3 × EF |

- **Evaluaciones continuas:** Controles de lectura, entrega de ejercicios de programación, participación en foros y quiz semanales.
- **Examen parcial:** Cubre semanas 1-7 (fundamentos, word embeddings, RNN, atención).
- **Examen final:** Proyecto integrador (ej. construir un chatbot con RAG y desplegarlo como API).
- **Examen sustitutorio:** Semana 15, reemplaza la nota más baja entre parcial y final.

---

