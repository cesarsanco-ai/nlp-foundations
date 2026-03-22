# Curso de Procesamiento de Lenguaje Natural (NLP)
## Syllabus de Notebooks por Semana

**Carlos César Sánchez Coronel**

2026

---

## Introducción

Cada semana se trabajará con dos tipos de notebooks:

- **Notebook Conceptual (NB1):** Enfocado en la comprensión profunda. Se utilizan datos *dummy* (textos inventados, secuencias cortas) para operaciones matemáticas, visualización de conceptos lingüísticos, implementación de algoritmos desde cero y experimentación con parámetros de modelos y librerías (NLTK, spaCy, Hugging Face, PyTorch). Aquí se exploran desde tokenización hasta mecanismos de atención.
- **Notebook de Ejercicios (NB2):** Aplicación práctica sobre conjuntos de datos reales (IMDb, SQuAD, corpora de noticias, etc.). Se plantean problemas concretos de clasificación, generación, extracción de información, etc., donde el estudiante debe aplicar lo aprendido, evaluar métricas y justificar decisiones.

---

## Semana 1: Fundamentos Lingüísticos y Primeros Pasos con NLP

### Propósito
Introducir al estudiante en el campo del NLP, sus desafíos y las herramientas básicas de procesamiento. Se exploran los niveles del lenguaje y se realiza una primera toma de contacto con NLTK y spaCy.

### Notebook Conceptual (NB1) – Explorando el Lenguaje con Datos Dummy

- **Datos:** Frases inventadas, oraciones con ambigüedad léxica y estructural.
- **Actividades:**
  1. Definir un pequeño corpus de oraciones y etiquetarlas manualmente con Part-of-Speech (sustantivo, verbo, etc.).
  2. Usar NLTK y spaCy para obtener automáticamente los POS tags y comparar.
  3. Visualizar árboles de dependencia con spaCy (displacy).
  4. Identificar entidades nombradas (NER) en textos dummy.
  5. Discutir la ambigüedad: ejemplos de misma palabra con diferente significado según contexto.
- **Conceptos:** Morfología, sintaxis, semántica, pragmática, POS tagging, NER, parsing.
- **Herramientas:** NLTK, spaCy, displacy.

### Notebook de Ejercicios (NB2) – Análisis de un Corpus Real

- **Dataset:** Fragmento de Brown Corpus (NLTK) o noticias cortas.
- **Actividades:**
  1. Cargar el corpus y realizar estadísticas básicas (número de oraciones, palabras, vocabulario).
  2. Aplicar POS tagging y NER con spaCy.
  3. Identificar las entidades más frecuentes.
  4. Reflexionar sobre los desafíos del lenguaje no estructurado.

---

## Semana 2: Preprocesamiento de Texto: Tokenización, Lematización y Expresiones Regulares

### Propósito
Dominar las técnicas de limpieza y normalización de texto, incluyendo tokenización a nivel de palabra y subpalabra, stemming, lematización y uso de regex.

### Notebook Conceptual (NB1) – Manipulación de Texto Dummy

- **Datos:** Textos inventados que incluyen URLs, emojis, números, mayúsculas, palabras con prefijos/sufijos.
- **Actividades:**
  1. Implementar tokenización manual con Python (split, expresiones regulares).
  2. Comparar tokenizadores de NLTK, spaCy y Hugging Face (BERT tokenizer).
  3. Aplicar stemming con PorterStemmer y SnowballStemmer; comparar resultados.
  4. Aplicar lematización con WordNetLemmatizer y spaCy; observar diferencias con stemming.
  5. Limpiar texto usando regex: eliminar URLs, menciones, caracteres especiales.
  6. Introducir tokenización por subpalabras: mostrar cómo BPE y WordPiece dividen palabras poco frecuentes.
- **Conceptos:** OOV, BPE, WordPiece, stemming vs lematización.
- **Herramientas:** re, NLTK, spaCy, tokenizers (Hugging Face).

### Notebook de Ejercicios (NB2) – Preprocesamiento de Reseñas de Películas

- **Dataset:** IMDb reviews (subconjunto).
- **Actividades:**
  1. Aplicar un pipeline de preprocesamiento completo: limpieza con regex, tokenización, eliminación de stopwords, lematización.
  2. Crear una función que normalice cualquier texto nuevo.
  3. Visualizar las palabras más frecuentes antes y después del preprocesamiento.

---

## Semana 3: Representación del Texto: BOW, TF-IDF y N-gramas

### Propósito
Transformar texto en vectores numéricos utilizando técnicas clásicas y entender sus limitaciones.

### Notebook Conceptual (NB1) – Construcción Manual de Vectores

- **Datos:** Tres oraciones muy cortas (ej. "el gato come pescado", "el perro come carne", "el gato come carne").
- **Actividades:**
  1. Construir manualmente el vocabulario y crear la matriz BOW (Bag of Words).
  2. Calcular TF-IDF paso a paso: frecuencia en documento, frecuencia inversa.
  3. Comparar los vectores BOW y TF-IDF para las oraciones; discutir qué palabras se ponderan más.
  4. Generar n-gramas (bigramas, trigramas) y observar cómo capturan contexto.
  5. Usar CountVectorizer y TfidfVectorizer de sklearn y verificar que los resultados coinciden con el cálculo manual.
- **Conceptos:** BOW, TF-IDF, n-gramas, representaciones dispersas.
- **Herramientas:** sklearn.feature_extraction.text.

### Notebook de Ejercicios (NB2) – Clasificación de Noticias con BOW/TF-IDF

- **Dataset:** 20 Newsgroups (sklearn) o noticias locales.
- **Actividades:**
  1. Extraer características con CountVectorizer y TfidfVectorizer.
  2. Entrenar un clasificador (regresión logística) y evaluar con accuracy.
  3. Probar distintos rangos de n-gramas y ver impacto.
  4. Identificar las palabras con mayor peso TF-IDF por categoría.

---

## Semana 4: Word Embeddings: Word2Vec y GloVe

### Propósito
Comprender la diferencia entre representaciones densas y dispersas, entrenar embeddings y explorar sus propiedades semánticas.

### Notebook Conceptual (NB1) – Entrenando Embeddings desde Cero

- **Datos:** Corpus pequeño (oraciones inventadas o fragmento de texto).
- **Actividades:**
  1. Explicar la arquitectura Skip-gram y CBOW con diagramas.
  2. Usar gensim para entrenar Word2Vec sobre el corpus pequeño.
  3. Visualizar los embeddings con PCA/t-SNE (matplotlib).
  4. Probar analogías: rey - hombre + mujer = ? (si el corpus lo permite).
  5. Cargar embeddings pre-entrenados de GloVe y explorar similitudes entre palabras.
  6. Comparar la cobertura de vocabulario entre Word2Vec propio y GloVe.
- **Conceptos:** Embeddings estáticos, Skip-gram, CBOW, matriz de co-ocurrencia (GloVe).
- **Herramientas:** gensim, numpy, matplotlib, sklearn.manifold.TSNE.

### Notebook de Ejercicios (NB2) – Búsqueda de Similitudes Semánticas

- **Dataset:** Corpus de Wikipedia (subconjunto) o textos de noticias.
- **Actividades:**
  1. Entrenar Word2Vec con más datos y evaluar calidad con analogías.
  2. Construir un sistema simple de búsqueda de palabras similares.
  3. Usar embeddings para encontrar documentos similares (promediando embeddings de palabras).

---

## Semana 5: Modelos Clásicos para NLP: Naive Bayes y SVM

### Propósito
Aplicar algoritmos clásicos de machine learning a tareas de clasificación de textos y comparar su rendimiento con enfoques modernos.

### Notebook Conceptual (NB1) – Clasificación con Datos Dummy

- **Datos:** Conjunto pequeño de textos inventados con dos categorías (ej. deportes y política).
- **Actividades:**
  1. Calcular probabilidades condicionales para Naive Bayes (manual) sobre el corpus pequeño.
  2. Implementar un clasificador Naive Bayes desde cero usando frecuencias.
  3. Entrenar GaussianNB y MultinomialNB con sklearn y comparar.
  4. Visualizar la frontera de decisión de SVM lineal en un espacio reducido (usando PCA sobre TF-IDF).
- **Conceptos:** Teorema de Bayes, independencia condicional, margen máximo.
- **Herramientas:** sklearn.naive_bayes, sklearn.svm.

### Notebook de Ejercicios (NB2) – Análisis de Sentimiento de Reseñas

- **Dataset:** IMDb reviews (clasificación positiva/negativa).
- **Actividades:**
  1. Preprocesar textos y representar con TF-IDF.
  2. Entrenar Naive Bayes y SVM lineal.
  3. Evaluar con precisión, recall, F1 y matriz de confusión.
  4. Comparar el rendimiento y velocidad de entrenamiento.

---

## Semana 6: Redes Neuronales para NLP y Embeddings Entrenables

### Propósito
Construir redes neuronales simples con PyTorch, introduciendo la capa de embedding y clasificadores basados en promedio de embeddings.

### Notebook Conceptual (NB1) – Clasificador con Embeddings Entrenables

- **Datos:** Frases cortas generadas (ej. "me gusta este producto", "es terrible").
- **Actividades:**
  1. Construir un vocabulario y mapear palabras a índices.
  2. Implementar una capa de embedding en PyTorch (nn.Embedding).
  3. Crear un modelo que promedie los embeddings de las palabras y pase por una capa lineal.
  4. Entrenar para clasificación binaria (positivo/negativo) con entropía cruzada.
  5. Visualizar la evolución de la pérdida y accuracy.
  6. Comparar embeddings pre-entrenados (GloVe) fijos vs. entrenables.
- **Conceptos:** Embedding layer, backpropagation, overfitting en NLP.
- **Herramientas:** PyTorch, torch.nn, torch.optim.

### Notebook de Ejercicios (NB2) – Clasificación de Sentimiento con PyTorch

- **Dataset:** IMDb (subconjunto balanceado).
- **Actividades:**
  1. Crear DataLoader con padding y atención a longitudes variables.
  2. Entrenar el modelo de promedio de embeddings.
  3. Evaluar en test y comparar con modelos clásicos (Naive Bayes, SVM).
  4. Experimentar con dropout y regularización.

---

## Semana 7: Redes Recurrentes (RNN, LSTM, GRU) para NLP

### Propósito
Modelar secuencias de texto capturando dependencias temporales mediante redes recurrentes.

### Notebook Conceptual (NB1) – RNN y LSTM con Datos Sintéticos

- **Datos:** Secuencias de números o caracteres (ej. predecir el siguiente número en [1,2,3,4,?]).
- **Actividades:**
  1. Implementar una RNN simple desde cero (o con PyTorch) y visualizar el estado oculto.
  2. Mostrar el problema del gradiente desvaneciente con secuencias largas (usando backpropagation manual).
  3. Construir una LSTM con PyTorch y comparar su capacidad para recordar información lejana.
  4. Entrenar una LSTM para clasificación de secuencias (ej. decidir si una secuencia de números es creciente o no).
- **Conceptos:** Estado oculto, vanishing gradient, puertas LSTM.
- **Herramientas:** PyTorch nn.RNN, nn.LSTM, nn.GRU.

### Notebook de Ejercicios (NB2) – Clasificación de Sentimiento con LSTM

- **Dataset:** IMDb o reviews de Yelp.
- **Actividades:**
  1. Construir un modelo LSTM con embeddings entrenables.
  2. Entrenar y comparar con el modelo de promedio de embeddings.
  3. Visualizar la atención (si se implementa) o las salidas ocultas.

---

## Semana 8: Modelos Seq2Seq y Atención

### Propósito
Implementar arquitecturas encoder-decoder con mecanismo de atención para tareas como traducción automática.

### Notebook Conceptual (NB1) – Traducción con Datos Dummy

- **Datos:** Pares de frases inventadas (ej. inglés "I love cats" → español "amo a los gatos").
- **Actividades:**
  1. Construir un encoder RNN que comprime la frase origen.
  2. Construir un decoder RNN que genera la frase destino.
  3. Implementar el mecanismo de atención (Bahdanau o Luong) paso a paso.
  4. Visualizar los pesos de atención para cada paso de generación.
  5. Entrenar el modelo en el corpus minúsculo y observar las traducciones.
- **Conceptos:** Encoder-decoder, contexto fijo, atención, BLEU.
- **Herramientas:** PyTorch, matplotlib para heatmaps de atención.

### Notebook de Ejercicios (NB2) – Traducción Inglés-Alemán (simplificada)

- **Dataset:** Multi30k (subconjunto de frases cortas).
- **Actividades:**
  1. Preprocesar y construir vocabularios.
  2. Entrenar un modelo Seq2Seq con atención.
  3. Evaluar con BLEU score usando sacrebleu.

---

## Semana 9: Transformers: Atención Multi-Head y Positional Encoding

### Propósito
Comprender la arquitectura del transformer desde cero, implementando self-attention y positional encoding.

### Notebook Conceptual (NB1) – Implementación de Self-Attention

- **Datos:** Secuencias de vectores aleatorios (simulan embeddings de palabras).
- **Actividades:**
  1. Calcular self-attention: matrices Q, K, V, softmax sobre puntuaciones.
  2. Implementar multi-head attention concatenando cabezas.
  3. Añadir positional encoding (seno/coseno) a los embeddings.
  4. Construir un bloque transformer completo (atención + feed-forward + residual + layer norm).
  5. Probar la propagación hacia adelante con datos dummy.
- **Conceptos:** Self-attention, multi-head, positional encoding, residual connections.
- **Herramientas:** PyTorch, numpy.

### Notebook de Ejercicios (NB2) – Clasificación de Texto con Transformer (Encoder)

- **Dataset:** IMDb o AG News.
- **Actividades:**
  1. Usar la implementación de transformer encoder de PyTorch (nn.TransformerEncoder) o construir una propia.
  2. Entrenar para clasificación y comparar con LSTM.
  3. Analizar la atención en diferentes cabezas.

---

## Semana 10: Modelos Pre-entrenados: BERT y GPT – Fine-tuning

### Propósito
Utilizar la librería Hugging Face para cargar modelos pre-entrenados y fine-tunearlos en tareas específicas.

### Notebook Conceptual (NB1) – Explorando BERT y GPT

- **Datos:** Una oración cualquiera.
- **Actividades:**
  1. Cargar el tokenizer de BERT (bert-base-uncased) y tokenizar una oración.
  2. Inspeccionar los input_ids, attention_mask y token type ids.
  3. Pasar por el modelo BERT y obtener los embeddings de cada token y el [CLS].
  4. Generar texto con GPT-2 usando pipeline.
  5. Comparar la representación contextual de una palabra en diferentes oraciones.
- **Conceptos:** MLM, NSP, autoregresivo, fine-tuning, tokenizers de subpalabras.
- **Herramientas:** transformers (Hugging Face), torch.

### Notebook de Ejercicios (NB2) – Fine-tuning de BERT para Clasificación

- **Dataset:** IMDb o cualquier dataset de clasificación de textos.
- **Actividades:**
  1. Fine-tunear BERT para clasificación binaria usando Trainer o entrenamiento manual.
  2. Evaluar en test y comparar con modelos clásicos y LSTM.
  3. Guardar el modelo fine-tuneado y subirlo al Hugging Face Hub (opcional).

---

## Semana 11: Tareas Avanzadas: NER, Question Answering, Summarization

### Propósito
Aplicar modelos pre-entrenados a tareas específicas usando pipelines y fine-tuning.

### Notebook Conceptual (NB1) – Pipelines de Hugging Face

- **Datos:** Texto inventado con entidades, preguntas simples.
- **Actividades:**
  1. Usar pipeline("ner") para extraer entidades.
  2. Usar pipeline("question-answering") con un contexto y una pregunta.
  3. Usar pipeline("summarization") en un párrafo.
  4. Analizar los resultados y umbrales de confianza.
- **Conceptos:** NER, SQuAD, ROUGE, extractive vs abstractive summarization.
- **Herramientas:** transformers, datasets (para métricas).

### Notebook de Ejercicios (NB2) – Fine-tuning para NER o QA

- **Dataset:** CoNLL-2003 (NER) o SQuAD (QA).
- **Actividades:**
  1. Fine-tunear BERT para NER usando Hugging Face.
  2. Evaluar con métricas por entidad.
  3. (Opcional) Fine-tunear para QA y evaluar con exact match y F1.

---

## Semana 12: RAG (Retrieval-Augmented Generation) y Bases de Datos Vectoriales

### Propósito
Diseñar sistemas que combinan recuperación de información con generación para responder preguntas sobre documentos propios.

### Notebook Conceptual (NB1) – Búsqueda Semántica con FAISS

- **Datos:** Conjunto pequeño de documentos (ej. párrafos de Wikipedia).
- **Actividades:**
  1. Generar embeddings de los documentos usando Sentence Transformers.
  2. Construir un índice FAISS y almacenar los embeddings.
  3. Dada una pregunta, obtener el embedding, buscar los documentos más similares.
  4. Pasar el documento recuperado a un modelo generativo (GPT-2) junto con la pregunta para generar respuesta.
  5. Evaluar la relevancia de los documentos recuperados.
- **Conceptos:** RAG, bases vectoriales, FAISS, Sentence Transformers.
- **Herramientas:** sentence-transformers, faiss, transformers.

### Notebook de Ejercicios (NB2) – Chatbot sobre Documentos Propios

- **Dataset:** PDFs o artículos propios (por ejemplo, política de empresa).
- **Actividades:**
  1. Crear un pipeline completo: chunking, embeddings, FAISS, recuperación, generación.
  2. Probar el chatbot con preguntas reales.
  3. Evaluar cualitativamente las respuestas.

---

## Semana 13: Prompt Engineering y Optimización (LoRA, Cuantización)

### Propósito
Dominar técnicas de prompting y métodos eficientes para adaptar y optimizar LLMs.

### Notebook Conceptual (NB1) – Experimentos con Prompts

- **Datos:** Preguntas variadas (matemáticas, razonamiento, creatividad).
- **Actividades:**
  1. Probar zero-shot, few-shot y chain-of-thought en un modelo como GPT-2 o Llama (vía Hugging Face).
  2. Comparar respuestas y analizar la mejora con ejemplos.
  3. Introducir LoRA: cargar un modelo base y aplicar PEFT para fine-tuning eficiente en un dataset pequeño.
  4. Cuantizar un modelo con torch.ao (INT8) y medir reducción de tamaño y velocidad.
- **Conceptos:** In-context learning, LoRA, adaptadores, cuantización, ONNX.
- **Herramientas:** peft, bitsandbytes, torch.ao, onnx.

### Notebook de Ejercicios (NB2) – Fine-tuning Eficiente con LoRA

- **Dataset:** Instrucciones o diálogos (ej. Alpaca).
- **Actividades:**
  1. Fine-tunar un modelo pequeño (como GPT-2) con LoRA para seguir instrucciones.
  2. Evaluar la calidad de las respuestas antes y después.
  3. Exportar a ONNX y medir latencia.

---

## Semana 14: Despliegue de Modelos NLP (MLOps)

### Propósito
Llevar un modelo NLP a producción: creación de API, contenerización y monitoreo básico.

### Notebook Conceptual (NB1) – API con FastAPI y Docker

- **Datos:** Modelo fine-tuneado de semanas anteriores (ej. clasificador de sentimiento).
- **Actividades:**
  1. Serializar el modelo con torch.save y tokenizer con save_pretrained.
  2. Crear una aplicación FastAPI con un endpoint /predict que reciba texto y devuelva la clase.
  3. Probar localmente con requests desde el notebook.
  4. Escribir un Dockerfile y construir la imagen.
  5. Ejecutar el contenedor y probar el endpoint.
- **Conceptos:** API REST, serialización, contenedores, latencia, throughput.
- **Herramientas:** FastAPI, uvicorn, docker, requests.

### Notebook de Ejercicios (NB2) – Monitoreo de Deriva

- **Datos:** Nuevos textos que simulan un cambio en la distribución (drift).
- **Actividades:**
  1. Desplegar la API localmente.
  2. Enviar lotes de textos y registrar predicciones.
  3. Usar evidently o alibi-detect para comparar la distribución de las predicciones con las originales.
  4. Detectar si hay drift y discutir acciones.