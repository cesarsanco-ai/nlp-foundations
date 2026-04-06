
# Sesión 1: Introducción a NLP y Fundamentos Lingüísticos

## 1. Introducción y Logro de la Sesión
El objetivo es comprender el alcance del **Procesamiento del Lenguaje Natural (NLP)**, sus aplicaciones en la industria y los conceptos lingüísticos básicos que permiten el tratamiento automático del lenguaje humano.

### 1.1. Definición y Desafíos
El NLP es una subdisciplina de la **Inteligencia Artificial** que busca dotar a las computadoras de la capacidad de entender, interpretar y generar lenguaje humano de manera útil. A diferencia de los datos estructurados, el lenguaje presenta desafíos únicos:
* **Ambigüedad**: Una misma palabra tiene múltiples significados según el contexto.
* **Creatividad**: El lenguaje evoluciona; surgen nuevas palabras y expresiones constantemente.
* **Dependencia del contexto**: El significado de una oración puede depender de lo dicho anteriormente.
* **Conocimiento de mundo**: Muchas expresiones requieren información extralingüística para ser comprendidas.

### 1.2. Breve Historia del NLP
| Época | Hitos y Enfoques |
| :--- | :--- |
| **1950s - 1960s** | Enfoques basados en reglas y sistemas expertos. Destaca el experimento de Georgetown (1954) y **ELIZA** (1966), el primer chatbot que simulaba un terapeuta. |
| **1970s** | **SHRDLU**: Sistema que comprendía lenguaje en un mundo de bloques, demostrando la necesidad de entender el entorno. |
| **1980s - 1990s** | Auge de los métodos estadísticos y el uso de corpus anotados para modelos probabilísticos. |
| **2000s** | Machine Learning clásico aplicado a texto, como Naive Bayes y SVM. Uso de recursos como WordNet. |
| **2010s** | Introducción de **Word Embeddings** (Word2Vec, GloVe) y representaciones densas mediante redes neuronales. |
| **2017 - Presente** | Revolución de los **Transformers** (BERT, GPT) y el surgimiento de los modelos fundacionales. |

---

## 2. Niveles del Lenguaje
Para procesar el lenguaje, la lingüística computacional lo divide en niveles de complejidad:

1.  **Morfología**: Estudia la estructura interna de las palabras y sus **morfemas** (unidades mínimas con significado).
    * *Tareas*: Segmentación, Lematización (forma canónica) y Stemming (raíz aproximada).
2.  **Sintaxis**: Estudia cómo se combinan las palabras para formar oraciones gramaticales mediante reglas de orden y concordancia.
3.  **Semántica**: Se ocupa del significado.
    * *Semántica Léxica*: Significado de palabras individuales (sinónimos, antónimos).
    * *Semántica Composicional*: Cómo se forma el significado de la oración al combinar palabras.
4.  **Pragmática**: Estudia el uso del lenguaje en contexto, incluyendo la ironía, el sarcasmo y las intenciones del hablante.

---

## 3. Tareas Fundamentales y Formalización

### 3.1. Part-of-Speech (POS) Tagging
Consiste en asignar a cada palabra su categoría gramatical (sustantivo, verbo, adjetivo).
* **Formalización Matemática**: Se busca la secuencia de etiquetas $t$ más probable para una secuencia de palabras $w$ mediante el teorema de Bayes:
    $$\hat{t}_1^n = \arg\max_{t_1^n} \frac{P(w_1^n | t_1^n) P(t_1^n)}{P(w_1^n)}$$
* **Modelos**: Modelos de Markov Ocultos (**HMM**), que estiman probabilidades de transición y emisión, y modelos de aprendizaje profundo (BiLSTM, Transformers).

### 3.2. Parsing (Análisis Sintáctico)
Proceso de determinar la estructura sintáctica de una oración según una gramática formal.
* **Parsing de Constituyentes**: Construye árboles jerárquicos basados en grupos de frases (Sintagma Nominal, Verbal).
* **Parsing de Dependencias**: Crea un grafo de relaciones binarias entre palabras. Es ideal para lenguas con orden libre y está más ligado a la semántica.
    

---

## 4. Corpus y Datasets Anotados
Un **corpus** es una colección estructurada de textos utilizada para investigación y entrenamiento de modelos. Los modernos deben seguir los **principios FAIR**: *Findable* (Localizable), *Accessible* (Accesible), *Interoperable* (Interoperable) y *Reusable* (Reutilizable).

### Ejemplos de la investigación actual:
* **RareDis**: Corpus para identificar enfermedades raras y manifestaciones clínicas en textos médicos (1,041 textos de Orphanet).
* **SAMSum**: Más de 16,000 diálogos de chat con resúmenes escritos por humanos para entrenamiento de resumen abstractivo.
* **Petro NLP**: Recursos para la industria del petróleo (en portugués), incluyendo el treebank **PetroGold** y el corpus de entidades **PetroNER**.
* **ELEXIS**: Corpus semántico de 2 millones de palabras para los idiomas oficiales de la Unión Europea.
* **NLUCat**: 12,000 instrucciones en catalán para asistentes virtuales, enfocado en necesidades de personas vulnerables.

---

## 5. Aplicaciones en la Industria
* **Asistentes Virtuales**: Clasificación de intenciones y extracción de entidades.
* **Análisis de Sentimiento**: Clasificación de polaridad y detección de emociones en redes sociales.
* **Extracción de Información**: Conversión de datos no estructurados (PDF, documentos legales) en información procesable. En industrias como la del petróleo, el 80% de los datos nuevos son no estructurados.
* **Resumen Automático**: Puede ser extractivo (selecciona frases) o abstractivo (genera texto nuevo).

---

## 6. Desafíos y Preparación para Entrevistas
| Desafío | Descripción |
| :--- | :--- |
| **Polisemia** | Una palabra con muchos significados; se resuelve con modelos contextuales como BERT. |
| **Conocimiento de Mundo** | Entender entidades y sus relaciones (ej. "El Papa visitó Barcelona"); se aborda con **Grafos de Conocimiento**. |
| **Escasez de Recursos** | Falta de datos para lenguas minoritarias; se soluciona con *Transfer Learning*. |
| **Sesgos** | Los modelos aprenden prejuicios de los datos; requiere un curado cuidadoso y métricas de equidad. |

