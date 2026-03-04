\documentclass[12pt,a4paper,openany,oneside]{book}

% --- Paquetes ---
\usepackage[utf8]{inputenc}
\usepackage[spanish, es-noshorthands]{babel}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{colortbl}
\usepackage{multirow}
\usepackage{hhline}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, shapes}
\pgfplotsset{compat=1.18}

\geometry{margin=2.5cm}

% --- Colores y estilos para código Python ---
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstset{
    language=Python,
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    showstringspaces=false
}

% --- Estilo de cabecera y pie ---
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyhead[L]{\small Carlos César Sánchez Coronel}
\fancyhead[R]{\small Sesión 2: Preprocesamiento de Texto}
\fancyfoot[L]{\small Carlos César Sánchez Coronel}
\fancyfoot[C]{\thepage}

% --- Portada ---
\title{
    \textbf{Sesión 2} \\ 
    \Huge \textbf{PREPROCESAMIENTO DE TEXTO} \\
    \Large De texto crudo a datos listos para modelar
}
\author{
    \small Por \\ \vspace{0.2cm}
    \Large \textsc{Carlos César Sánchez Coronel}
}
\date{2026}

\begin{document}

\maketitle
\tableofcontents
\addcontentsline{toc}{chapter}{Índice general}

% ------------------------------------------------------------------
% CAPÍTULO 2: SESIÓN 2 - PREPROCESAMIENTO DE TEXTO
% ------------------------------------------------------------------
\chapter{Preprocesamiento de Texto}

En la sesión anterior se establecieron los fundamentos lingüísticos del NLP. Ahora se aborda el primer paso práctico en cualquier pipeline de NLP: transformar el texto crudo en una representación estructurada que pueda ser procesada por algoritmos. El preprocesamiento determina en gran medida la calidad de los modelos posteriores. Esta sesión cubre desde la tokenización básica hasta técnicas avanzadas de segmentación en subpalabras, pasando por normalización, eliminación de stopwords y lematización.

\section{Logro de la sesión}
Aplicar técnicas de limpieza y normalización de texto para preparar datos para modelos de NLP, comprendiendo los fundamentos matemáticos y computacionales de cada técnica y su impacto en el rendimiento de los modelos.

\section{Introducción: el pipeline de preprocesamiento}

El texto que proviene del mundo real (redes sociales, documentos, transcripciones) es desordenado, ruidoso y no estructurado. El preprocesamiento tiene como objetivo transformarlo en una secuencia de unidades atómicas (tokens) limpia y normalizada que pueda ser alimentada a modelos estadísticos o neuronales. Un pipeline típico incluye:

\begin{enumerate}
    \item \textbf{Limpieza inicial}: eliminar caracteres no deseados, normalizar formato.
    \item \textbf{Tokenización}: segmentar el texto en unidades (palabras, oraciones, subpalabras).
    \item \textbf{Normalización}: convertir a minúsculas, manejar contracciones, etc.
    \item \textbf{Eliminación de stopwords}: filtrar palabras muy frecuentes sin significado.
    \item \textbf{Reducción morfológica}: stemming o lematización.
\end{enumerate}

Cada decisión en este pipeline afecta el vocabulario final, la capacidad de manejar palabras desconocidas y, en última instancia, la precisión del modelo.

\section{Tokenización}

La tokenización es el proceso de dividir un texto en unidades más pequeñas llamadas \textbf{tokens}. Es el paso fundamental del que dependen todos los demás.

\subsection{Tokenización por palabras (word tokenization)}
Es la forma más intuitiva: separar por espacios y signos de puntuación. Sin embargo, es más compleja de lo que parece debido a:
\begin{itemize}
    \item Contracciones: "don't" → ["do", "n't"] o ["don't"]?
    \item Puntuación: "hola!" → ["hola", "!"] o ["hola!"]?
    \item Lenguas sin espacios: chino, japonés.
\end{itemize}

\textbf{Implementaciones comunes}: NLTK \texttt{word\_tokenize}, spaCy, Stanford CoreNLP.

\subsection{Tokenización por oraciones (sentence tokenization)}
Divide un texto en oraciones. Los desafíos incluyen la desambiguación del punto:
\begin{itemize}
    \item "El Sr. Pérez llegó. ¿Cómo está?" → El punto después de "Sr." no indica fin de oración.
\end{itemize}
Los modelos suelen usar reglas basadas en abreviaturas o modelos de ML entrenados.

\subsection{Tokenización por subpalabras (subword tokenization)}
Los modelos modernos (BERT, GPT) no tokenizan por palabras completas, sino por subpalabras. Esto resuelve el problema de palabras fuera de vocabulario (OOV) y permite representar palabras raras como combinación de subpalabras conocidas.

\subsubsection{Byte-Pair Encoding (BPE)}
BPE es un algoritmo de compresión adaptado a la tokenización. Funciona de la siguiente manera:

\begin{enumerate}
    \item Inicializar el vocabulario con todos los caracteres individuales (bytes).
    \item Contar frecuencias de pares de símbolos adyacentes en el corpus.
    \item Fusionar el par más frecuente y añadirlo al vocabulario.
    \item Repetir hasta alcanzar el tamaño de vocabulario deseado.
\end{enumerate}

\textbf{Ejemplo numérico}:
Corpus: "low low low low low lower lowest" (simplificado)
\begin{enumerate}
    \item Inicial: {'l','o','w','e','r','s','t'}
    \item Contar pares: ('l','o'): 6, ('o','w'): 6, ('w',''): 6, ...
    \item Fusionar 'l'+'o' → 'lo'. Nuevo vocabulario: {'l','o','w','e','r','s','t','lo'}
    \item Recontar: ('lo','w'): 6 → fusionar 'lo'+'w' → 'low'
    \item Así sucesivamente hasta obtener 'low', 'lower', 'lowest' como tokens.
\end{enumerate}

BPE se usa en GPT y RoBERTa.

\subsubsection{WordPiece}
Similar a BPE pero en lugar de frecuencia bruta, fusiona el par que maximiza la probabilidad del lenguaje:
\[
\text{score}(a,b) = \frac{\text{freq}(ab)}{\text{freq}(a) \cdot \text{freq}(b)}
\]
Esto tiende a crear tokens más lingüísticamente significativos. WordPiece se usa en BERT.

\subsubsection{Unigram Language Model Tokenization}
Propone un vocabulario de subpalabras y asigna probabilidades según un modelo de lenguaje unigrama. Se entrena con el algoritmo EM (Expectation-Maximization) y se usa en modelos como SentencePiece.

\subsection{Impacto computacional}
La tokenización por subpalabras produce secuencias más largas que la tokenización por palabras, pero maneja mejor el vocabulario abierto. En los Transformers, la longitud máxima de secuencia es un hiperparámetro crítico.

\section{Normalización}

La normalización reduce la variabilidad superficial del texto sin perder significado.

\subsection{Minúsculas (lowercasing)}
Convertir todo el texto a minúsculas. Es la técnica más simple y casi siempre beneficiosa, excepto cuando el caso es informativo (ej. nombres propios en NER).

\subsection{Eliminación de caracteres especiales}
\begin{itemize}
    \item Eliminar signos de puntuación (aunque a veces son útiles: "¿?" puede indicar pregunta).
    \item Eliminar caracteres no imprimibles, Unicode no estándar.
    \item Normalizar Unicode (ej. 'café' vs 'cafe' con tilde vs combinada).
\end{itemize}

\textbf{Formalmente}: se define un conjunto de caracteres permitidos \( \mathcal{C} \) y se filtra:
\[
\text{texto}_{\text{norm}} = \{ c \in \text{texto} \mid c \in \mathcal{C} \}
\]

\subsection{Manejo de URLs y menciones}
En redes sociales, URLs, menciones (@usuario) y hashtags suelen eliminarse o sustituirse por tokens especiales (ej. <URL>, <USER>). Esto reduce el vocabulario y el ruido.

\subsection{Manejo de emojis y emoticonos}
Los emojis pueden ser relevantes para análisis de sentimiento. Se pueden:
\begin{itemize}
    \item Eliminar.
    \item Convertir a texto (ej. :) → "smile").
    \item Tratar como tokens especiales.
\end{itemize}

\subsection{Expresiones regulares (regex) para limpieza avanzada}
Las expresiones regulares son una herramienta matemática y computacional para describir patrones en texto. Se basan en la teoría de autómatas finitos.

\textbf{Ejemplos prácticos}:
\begin{lstlisting}[language=Python]
import re
# Eliminar URLs
texto = re.sub(r'http\S+', '', texto)
# Eliminar caracteres no alfabéticos
texto = re.sub(r'[^a-zA-Z\s]', '', texto)
# Normalizar espacios múltiples
texto = re.sub(r'\s+', ' ', texto)
\end{lstlisting}

\textbf{Fundamento matemático}: Una expresión regular define un lenguaje regular, que puede ser reconocido por un autómata finito determinista (DFA). La complejidad de la coincidencia es \(O(n)\) en el tamaño del texto, lo que las hace muy eficientes.

\section{Eliminación de stopwords}

Las \textbf{stopwords} son palabras muy frecuentes que aportan poco significado (artículos, preposiciones, conjunciones). Eliminarlas puede reducir el ruido y la dimensionalidad.

\subsection{Listas de stopwords}
Existen listas predefinidas para cada idioma en NLTK, spaCy, etc. Sin embargo, en dominios específicos, palabras como "cliente" podrían ser stopwords en un corpus de atención al cliente.

\textbf{Advertencia}: En modelos modernos basados en atención (Transformers), eliminar stopwords puede no ser beneficioso porque el modelo puede aprender a ignorarlas por sí mismo.

\subsection{Enfoques alternativos}
\begin{itemize}
    \item Usar frecuencia inversa de documento (IDF) para ponderar términos: las stopwords tienen bajo IDF.
    \item Mantener todas las palabras pero usar subword tokenization que las tratará como tokens separados.
\end{itemize}

\section{Stemming vs. Lemmatization}

Ambas técnicas reducen palabras a una forma base, pero con diferencias fundamentales.

\subsection{Stemming}
Algoritmo heurístico que elimina sufijos para obtener una raíz (stem). No necesita diccionario.

\textbf{Ejemplo}:
\begin{itemize}
    \item "running", "runner", "ran" → "run" (todos al mismo stem)
    \item "studies", "studying" → "studi"
\end{itemize}

\textbf{Algoritmos}:
\begin{itemize}
    \item \textbf{Porter Stemmer}: basado en reglas lingüísticas, 5 fases de aplicación.
    \item \textbf{Snowball Stemmer}: mejora del Porter, soporta varios idiomas.
    \item \textbf{Lancaster Stemmer}: más agresivo, puede producir stems muy cortos.
\end{itemize}

\textbf{Ventajas}: rápido, simple, no requiere recursos externos.
\textbf{Desventajas}: produce stems no lingüísticos, puede generar ambigüedad.

\subsection{Lematización}
Reduce a la forma canónica (lema) utilizando un diccionario morfológico y análisis del contexto (part-of-speech).

\textbf{Ejemplo}:
\begin{itemize}
    \item "running" (verbo) → "run"
    \item "studies" (sustantivo) → "study"
    \item "studies" (verbo) → "study" (depende del contexto)
\end{itemize}

\textbf{Ventajas}: produce palabras reales del idioma, más precisa.
\textbf{Desventajas}: más lenta, requiere recursos (WordNet, modelos de POS).

\subsection{Comparación formal}
\begin{table}[h]
\centering
\begin{tabular}{|l|l|l|}
\hline
\textbf{Criterio} & \textbf{Stemming} & \textbf{Lematización} \\
\hline
Velocidad & Alta & Baja \\
Recursos & Ninguno & Diccionario, modelo POS \\
Precisión lingüística & Baja & Alta \\
Manejo de irregularidades & No & Sí (ej. "mejor" → "bueno") \\
Uso típico & Búsqueda de información, análisis rápido & NLP profundo, chatbots \\
\hline
\end{tabular}
\caption{Comparación entre stemming y lematización.}
\end{table}

\subsection{¿Cuándo usar cada una?}
\begin{itemize}
    \item \textbf{Stemming}: en sistemas de recuperación de información (motores de búsqueda) donde la velocidad es crítica y el usuario no nota la diferencia.
    \item \textbf{Lematización}: en tareas que requieren comprensión semántica (análisis de sentimiento, NER, traducción).
\end{itemize}

\textbf{Ejemplo práctico}: En un buscador, el usuario que escribe "running" espera ver resultados con "run", "runner", etc. El stemming agrupa todos bajo "run". En un chatbot, entender "corrió" como "correr" requiere lematización.

\section{Desafíos en NLP: Out-of-Vocabulary (OOV)}

\subsection{Definición}
Una palabra es \textbf{OOV} si no está presente en el vocabulario del modelo. Esto ocurre por:
\begin{itemize}
    \item Palabras raras o técnicas.
    \item Errores tipográficos.
    \item Neologismos.
    \item Lenguas con morfología rica.
\end{itemize}

\subsection{Soluciones tradicionales}
\begin{itemize}
    \item Reemplazar por un token especial <UNK>.
    \item Usar backing-off (n-gramas).
    \item Desventaja: pérdida de información.
\end{itemize}

\subsection{Soluciones modernas: subword tokenization}
Los métodos de subpalabras resuelven OOV al descomponer palabras desconocidas en subpalabras conocidas. Por ejemplo, "transformers" puede descomponerse como ["transform", "ers"] si ambas subpalabras están en el vocabulario.

\textbf{Ejemplo con BPE}:
\begin{itemize}
    \item Vocabulario: {"low", "lowest", "new", "er"}
    \item Palabra OOV: "lower" → tokenizada como "low" + "er"
\end{itemize}

Esto permite que el modelo maneje cualquier palabra, incluso las no vistas, con una representación basada en partes.

\section{Pipeline completo de preprocesamiento: ejemplo concreto}

\subsection{Datos de entrada}
Texto: "I LOVE NLP!!! Check out https://example.com for more info @nlp_expert #nlp"

\subsection{Paso 1: Limpieza con regex}
\begin{lstlisting}[language=Python]
import re
text = "I LOVE NLP!!! Check out https://example.com for more info @nlp_expert #nlp"
text = re.sub(r'http\S+', '<URL>', text)  # URLs -> <URL>
text = re.sub(r'@\S+', '<USER>', text)     # menciones -> <USER>
text = re.sub(r'#\S+', '<HASHTAG>', text)  # hashtags -> <HASHTAG>
text = re.sub(r'[!?.]+', '', text)         # eliminar puntuación
print(text)
# "I LOVE NLP Check out <URL> for more info <USER> <HASHTAG>"
\end{lstlisting}

\subsection{Paso 2: Minúsculas}
\begin{lstlisting}[language=Python]
text = text.lower()
print(text)
# "i love nlp check out <url> for more info <user> <hashtag>"
\end{lstlisting}

\subsection{Paso 3: Tokenización con BPE (simulado)}
Vocabulario BPE podría tener: {"i", "love", "nlp", "check", "out", "<url>", "for", "more", "info", "<user>", "<hashtag>"} – todas las palabras están en vocabulario.

\subsection{Paso 4: Eliminación de stopwords (opcional)}
Stopwords comunes: {"i", "for", "out"}. Eliminándolas:
Tokens restantes: ["love", "nlp", "check", "<url>", "more", "info", "<user>", "<hashtag>"]

\subsection{Paso 5: Lematización (simulado)}
Con lematizador: "love" → "love", "check" → "check", "more" → "more", "info" → "information" (depende del contexto). No cambia mucho en este ejemplo.

\subsection{Paso 6: Subword tokenization real con BPE}
Si se usa un tokenizador BPE entrenado, podría descomponer "nlp" como ["nl", "p"] si no está en vocabulario, aunque normalmente "nlp" sería un token.

\section{Implementación en Python con librerías}

\subsection{Uso de NLTK}
\begin{lstlisting}[language=Python]
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "I love NLP. It's fascinating!"
tokens = word_tokenize(text)
tokens_lower = [t.lower() for t in tokens]
stop_words = set(stopwords.words('english'))
tokens_filtered = [t for t in tokens_lower if t not in stop_words]

stemmer = PorterStemmer()
stems = [stemmer.stem(t) for t in tokens_filtered]

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens_filtered]
\end{lstlisting}

\subsection{Uso de spaCy (más moderno)}
\begin{lstlisting}[language=Python]
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("I love NLP. It's fascinating!")

tokens = [token.text for token in doc]
lemmas = [token.lemma_ for token in doc]
pos_tags = [token.pos_ for token in doc]
\end{lstlisting}

\subsection{Uso de tokenizadores de subpalabras (HuggingFace)}
\begin{lstlisting}[language=Python]
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize("I love NLP!")
input_ids = tokenizer.convert_tokens_to_ids(tokens)
\end{lstlisting}

\section{Caso integrado: Preprocesamiento para análisis de sentimiento en Twitter}

\subsection{Problema}
Se tienen 100,000 tweets etiquetados como positivo/negativo. Se desea construir un clasificador.

\subsection{Pasos}
\begin{enumerate}
    \item \textbf{Limpieza}: eliminar URLs, menciones, caracteres no ASCII, normalizar emojis.
    \item \textbf{Normalización}: minúsculas, manejar contracciones (won't → will not).
    \item \textbf{Tokenización}: usar tokenizador de subpalabras (BPE) para manejar jerga de Twitter ("luv", "omg").
    \item \textbf{Opcional}: no eliminar stopwords porque el modelo puede aprender que "not" es importante.
    \item \textbf{Lematización}: no esencial si se usan subpalabras.
\end{enumerate}

\subsection{Evaluación}
Se compara la precisión con diferentes pipelines. Se observa que:
\begin{itemize}
    \item Eliminar URLs mejora la precisión (reduce ruido).
    \item Mantener "not" y "no" es crucial; eliminarlas empeora el F1-score.
    \item El tokenizador BPE maneja bien palabras como "bestttt" (tokenizada como "best" + "ttt").
\end{itemize}

\section{Preparación para entrevistas: preguntas típicas}

\subsection{Preguntas conceptuales}
\begin{itemize}
    \item \textbf{"¿Cuándo usar stemming y cuándo lematización?"}
    Responder con la tabla comparativa: velocidad vs precisión, contexto de aplicación.
    \item \textbf{"¿Qué es BPE y cómo funciona?"}
    Explicar el algoritmo paso a paso, mencionar que se usa en GPT.
    \item \textbf{"¿Cómo manejas las palabras fuera de vocabulario (OOV)?"}
    Hablar de tokenización por subpalabras como solución moderna.
    \item \textbf{"¿Siempre eliminas stopwords?"}
    No, depende del modelo. En modelos lineales puede ayudar, en Transformers no es necesario.
\end{itemize}

\subsection{Preguntas prácticas}
\begin{itemize}
    \item \textbf{"Escribe una expresión regular para eliminar URLs de un texto."}
    \texttt{r'http\S+'} o más completa \texttt{r'https?://\S+|www\.\S+'}.
    \item \textbf{"¿Cómo tokenizarías un texto en chino?"}
    No se puede por espacios; se usan segmentadores específicos (Jieba) o modelos de subpalabras.
\end{itemize}

\section{Conexión con el resto del curso}
El preprocesamiento es el cimiento sobre el que se construyen:
\begin{itemize}
    \item \textbf{Sesión 3}: Representaciones vectoriales (BoW, TF-IDF) que dependen del vocabulario generado.
    \item \textbf{Sesión 4}: Modelos clásicos de clasificación, sensibles a la calidad de los tokens.
    \item \textbf{Sesión 5}: Word embeddings, que requieren un vocabulario bien definido.
    \item \textbf{Sesión 6 en adelante}: Redes neuronales y Transformers, que usan tokenizadores de subpalabras como los aquí descritos.
\end{itemize}

\section{Resumen}
\begin{itemize}
    \item La \textbf{tokenización} puede ser por palabras, oraciones o subpalabras. Los métodos de subpalabras (BPE, WordPiece) son el estándar actual.
    \item La \textbf{normalización} reduce ruido: minúsculas, eliminación de caracteres, manejo de URLs/emojis.
    \item Las \textbf{expresiones regulares} son una herramienta poderosa para limpieza.
    \item Las \textbf{stopwords} pueden eliminarse en modelos tradicionales, pero en deep learning no es necesario.
    \item \textbf{Stemming vs lematización}: el primero es rápido y heurístico, el segundo es preciso y lingüístico.
    \item El problema \textbf{OOV} se resuelve eficazmente con tokenización por subpalabras.
\end{itemize}

\end{document}