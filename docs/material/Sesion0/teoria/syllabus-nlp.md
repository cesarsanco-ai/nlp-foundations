# Sílabo del Curso **PROCESAMIENTO DE LENGUAJE NATURAL (NLP)**

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

## Semana 3: Modelos Estadísticos y Probabilísticos

### Logro de la sesión
Comprender y aplicar modelos probabilísticos para modelar lenguaje y resolver tareas de NLP clásico.

#### Conceptos
- Fundamentos de probabilidad en NLP: variables aleatorias, distribuciones y estimación.
- Modelos de lenguaje con n-gramas y suavizado (Laplace, Good-Turing).
- Teorema de Bayes aplicado a clasificación de texto.
- Modelos generativos vs. discriminativos en NLP.
- Evaluación básica de modelos probabilísticos (perplejidad, log-likelihood).

#### Aplicaciones y entrevistas
- Pregunta frecuente: "Explica cómo funciona Naive Bayes para clasificación de textos".
- Diferenciar el uso de modelos n-grama frente a modelos neuronales modernos.

#### Python
- Implementación de un clasificador Naive Bayes en `scikit-learn`.
- Construcción de un modelo n-grama simple y cálculo de probabilidades de secuencia.
- Comparación entre enfoques probabilísticos y representaciones básicas.

---

## Semana 4: Word Embeddings estáticos

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

## Semana 5: Clasificación de texto con ML clásico

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

## Semana 6: Embeddings contextuales (RNN/LSTM/GRU en NLP)

### Logro de la sesión
Modelar contexto en secuencias de texto mediante arquitecturas recurrentes y comparar su capacidad representacional.

#### Conceptos
- Limitaciones de embeddings estáticos ante polisemia y contexto.
- Redes recurrentes (RNN) y problema del gradiente desvaneciente.
- LSTM y GRU para modelar dependencias largas.
- Embeddings contextuales generados por el estado de la secuencia.
- Comparación conceptual con embeddings estáticos.

#### Aplicaciones y entrevistas
- Pregunta típica: "¿Por qué LSTM/GRU mejoran a una RNN vanilla en texto?"
- Identificar escenarios donde el contexto cambia el significado de una palabra.

#### Python
- Implementación de un clasificador secuencial con RNN/LSTM en PyTorch.
- Comparación rápida de resultados entre RNN, LSTM y GRU.
- Visualización del impacto del contexto en la representación de palabras.

---

## Semana 7: Modelo Seq2Seq y Mecanismos de Atención

### Logro de la sesión
Construir modelos encoder-decoder para tareas de transformación de secuencias e incorporar atención.

#### Conceptos
- Arquitectura encoder-decoder para secuencias.
- Limitación del vector de contexto fijo.
- Mecanismo de atención y alineamiento entrada-salida.
- Aplicaciones: traducción automática y resumen.
- Métricas de evaluación en generación secuencial (BLEU).

#### Aplicaciones y entrevistas
- Pregunta clave: "¿Qué problema resuelve la atención en Seq2Seq?"
- Entender por qué la atención habilita secuencias más largas y precisas.

#### Python
- Implementación de un modelo Seq2Seq con atención en PyTorch.
- Práctica de traducción simple con dataset reducido.
- Evaluación básica de calidad con BLEU.

---

## Semana 8: Arquitectura Transformer

### Logro de la sesión
Comprender la arquitectura transformer como base de los modelos modernos de NLP.

#### Conceptos
- Motivación histórica: de RNN/Seq2Seq a transformers.
- Visión general del encoder-decoder transformer.
- Self-attention como mecanismo central.
- Positional encoding y paralelización.
- Ventajas frente a arquitecturas recurrentes.

#### Aplicaciones y entrevistas
- Pregunta frecuente: "¿Por qué transformer reemplazó a RNN en muchas tareas?"
- Explicar el rol de positional encodings cuando no hay recurrencia.

#### Python
- Exploración guiada de bloques transformer con `transformers` y `torch`.
- Inspección de pesos de atención en ejemplos reales.
- Mini experimento comparativo en tiempo de entrenamiento/inferencia.

---

## Semana 9: Componentes del Transformer

### Logro de la sesión
Desglosar en detalle los componentes internos del transformer y su función matemática.

#### Conceptos
- Multi-head self-attention y scaled dot-product attention.
- Feed-forward networks por posición.
- Residual connections y layer normalization.
- Máscaras de atención (padding mask y causal mask).
- Diferencias entre encoder-only, decoder-only y encoder-decoder.

#### Aplicaciones y entrevistas
- Pregunta técnica: "¿Qué aporta el mecanismo multi-head frente a una sola cabeza?"
- Relacionar arquitectura con familias de modelos como BERT y GPT.

#### Python
- Implementación desde cero de self-attention y masking en PyTorch.
- Visualización de formas tensores en cada bloque.
- Ejercicios de interpretación de salidas intermedias.

---

## Semana 10: Modelos pre-entrenados (BERT, GPT y T5)

### Logro de la sesión
Comprender paradigmas de preentrenamiento y aplicar modelos fundacionales a distintas tareas de NLP.

#### Conceptos
- BERT: enfoque encoder-only y objetivos MLM/NSP.
- GPT: enfoque decoder-only y generación autorregresiva.
- T5: enfoque text-to-text para tareas unificadas.
- Prompting vs. fine-tuning clásico.
- Comparación de trade-offs según tarea, costo y latencia.

#### Aplicaciones y entrevistas
- Pregunta clave: "¿En qué casos conviene BERT, GPT o T5?"
- Argumentar elección de modelo según tipo de problema (clasificación, generación, traducción).

#### Python
- Uso de `pipeline` y `Trainer` de Hugging Face con modelos BERT/GPT/T5.
- Experimentos comparativos en una tarea de clasificación y otra generativa.
- Reporte simple de métricas y análisis de errores.

---

## Semana 11: Razonamiento y capacidades emergentes

### Logro de la sesión
Analizar capacidades emergentes de los LLMs y técnicas de razonamiento asistido por prompting.

#### Conceptos
- Capacidades emergentes en modelos de gran escala.
- Razonamiento paso a paso (chain-of-thought) y variantes.
- In-context learning y sensibilidad al prompt.
- Alucinaciones, factualidad y límites de razonamiento.
- Criterios de evaluación cualitativa y cuantitativa.

#### Aplicaciones y entrevistas
- Pregunta habitual: "¿Qué significa que una capacidad sea emergente en LLMs?"
- Distinguir razonamiento real de patrones espurios en respuestas.

#### Python
- Diseño de prompts para tareas de razonamiento lógico y multietapa.
- Evaluación de consistencia entre distintas estrategias de prompting.
- Análisis guiado de fallos y alucinaciones.

---

## Semana 12: Transfer Learning y adaptación

### Logro de la sesión
Aplicar estrategias de adaptación de modelos pre-entrenados a dominios y tareas específicas.

#### Conceptos
- Principios de transfer learning en NLP.
- Fine-tuning completo vs. fine-tuning parcial.
- Domain adaptation y task adaptation.
- Data-centric adaptation: selección, limpieza y balance de datos.
- Evaluación comparativa antes/después de adaptación.

#### Aplicaciones y entrevistas
- Pregunta frecuente: "¿Cómo adaptarías un modelo generalista a un dominio legal o médico?"
- Justificar estrategia de adaptación según presupuesto y datos disponibles.

#### Python
- Fine-tuning supervisado de un modelo pre-entrenado en un dataset de dominio.
- Comparación entre baseline sin adaptar y modelo adaptado.
- Documentación de decisiones de adaptación y resultados.

---

## Semana 13: Eficiencia en NLP (PEFT, Quantization)

### Logro de la sesión
Dominar técnicas de eficiencia para adaptar y desplegar modelos NLP con menor costo computacional.

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

## Semana 14: NLP Multilingüe y post-Transformers

### Logro de la sesión
Explorar NLP multilingüe y tendencias de arquitectura posteriores a transformer.

#### Conceptos
- Desafíos del NLP multilingüe: transferencia cruzada y recursos desbalanceados.
- Modelos multilingües (mBERT, XLM-R) y evaluación cross-lingual.
- Eficiencia y escalabilidad en escenarios globales.
- Panorama post-transformers: State Space Models, Mixture-of-Experts y arquitecturas híbridas.
- Tendencias de investigación y aplicaciones futuras.

#### Aplicaciones y entrevistas
- Pregunta clave: "¿Cómo abordarías una solución NLP para varios idiomas con pocos datos?"
- Identificar límites y oportunidades de las arquitecturas post-transformer.

#### Python
- Experimentos con inferencia multilingüe y análisis de sesgo por idioma.
- Uso de modelos multilingües de Hugging Face en tareas de clasificación/QA.
- Discusión técnica guiada sobre papers recientes post-transformers.
