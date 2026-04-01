
# Modelos Seq2Seq y Atención

## Introducción: problemas de secuencia a secuencia

En tareas de procesamiento del lenguaje natural, a menudo necesitamos transformar una secuencia de entrada en una secuencia de salida de longitud variable. Ejemplos:

- **Traducción automática**: inglés $\to$ francés.
- **Resumen automático**: documento largo $\to$ resumen corto.
- **Diálogo**: pregunta del usuario $\to$ respuesta.
- **Generación de preguntas**: texto + respuesta $\to$ pregunta.

Las redes recurrentes (RNN, LSTM, GRU) vistas anteriormente pueden procesar secuencias y mantener un estado que resume la información. Sin embargo, no están diseñadas para **generar** una nueva secuencia condicionada a la entrada, especialmente cuando las longitudes son diferentes.

### Problemas de RNN (contexto limitado)

Aunque las RNN y sus variantes con compuertas (LSTM, GRU) mitigan el problema del gradiente evanescente, su **contexto** sigue siendo limitado. El estado oculto final $\mathbf{h}_T$ tiende a enfatizar los últimos elementos de la secuencia, diluyendo la información de los primeros. Esto es crítico cuando la salida depende de partes tempranas de la entrada. Además, las RNN tradicionales producen una salida en cada paso (muchos-a-muchos), pero no pueden transformar una secuencia en otra de longitud diferente sin una arquitectura específica.

## Notación y variables del modelo

Para formalizar, definimos las variables que se utilizarán tanto en esta sección como en el contexto de las RNN previas. Recordemos que en RNN simples teníamos:

- $\mathbf{x}_t$: vector de entrada en el paso $t$.
- $\mathbf{h}_t$: estado oculto en el paso $t$.
- $\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$, $\mathbf{b}_h$: pesos y sesgos para la actualización del estado.
- $\mathbf{W}_{hy}$, $\mathbf{b}_y$: pesos y sesgos para la salida.

En el modelo Seq2Seq con atención, ampliamos esta notación:

- **Secuencia de entrada**: $\mathbf{x} = (x_1, x_2, \dots, x_T)$, donde cada $x_t$ es un token (por ejemplo, una palabra) de un vocabulario fuente $\mathcal{V}_X$.
- **Secuencia de salida**: $\mathbf{y} = (y_1, y_2, \dots, y_{T'})$, con $y_t \in \mathcal{V}_Y$ (vocabulario destino).
- **Embeddings**: $\mathbf{e}(x_t) \in \mathbb{R}^{d_e}$ es la representación vectorial de la palabra $x_t$ (similar a las capas de embedding usadas en RNN para NLP).
- **Encoder**: produce estados ocultos $\mathbf{h}_1, \mathbf{h}_2, \dots, \mathbf{h}_T$ a partir de la secuencia de entrada. Usaremos la misma notación que en RNN: $\mathbf{h}_t = \text{RNN}_\text{enc}(\mathbf{e}(x_t), \mathbf{h}_{t-1})$, con $\mathbf{h}_0 = \mathbf{0}$.
- **Vector de contexto fijo (inicial)**: $\mathbf{c}$ (un vector que resume toda la entrada). En la arquitectura básica, $\mathbf{c} = \mathbf{h}_T$.
- **Decoder**: produce estados ocultos $\mathbf{s}_1, \mathbf{s}_2, \dots, \mathbf{s}_{T'}$ a partir de la salida generada. Notación: $\mathbf{s}_t = \text{RNN}_\text{dec}(\mathbf{e}(y_{t-1}), \mathbf{s}_{t-1})$, con $\mathbf{s}_0 = \mathbf{c}$.
- **Atención**: introduce un vector de contexto dinámico $\mathbf{c}_t$ en cada paso $t$, calculado a partir de los estados del encoder $\mathbf{h}_i$ y el estado actual (o anterior) del decoder. Los pesos de atención se denotan $\alpha_{t,i}$, y cumplen $\sum_{i=1}^T \alpha_{t,i} = 1$.

Todos los parámetros aprendibles (matrices de pesos y sesgos) se denotarán con letras mayúsculas (por ejemplo, $\mathbf{W}_a$, $\mathbf{U}_a$, $\mathbf{v}_a$) para diferenciarlos de los estados.

## Arquitectura Seq2Seq: Encoder-Decoder

### Visión general

La arquitectura Seq2Seq, introducida por Sutskever et al. (2014), separa el proceso de **codificación** (lectura de la entrada) del de **decodificación** (generación de la salida). Ambos componentes son redes recurrentes, típicamente LSTM o GRU, que pueden manejar secuencias de longitud variable.

### Funcionamiento del Encoder

El encoder procesa la secuencia de entrada paso a paso:

$$ \mathbf{h}_t = \text{RNN}_\text{enc}(\mathbf{e}(x_t), \mathbf{h}_{t-1}), \quad t = 1,\dots,T, $$

con $\mathbf{h}_0 = \mathbf{0}$ (vector de ceros). El estado final $\mathbf{h}_T$ se usa como **vector de contexto** $\mathbf{c}$ que resume la entrada. En la práctica, si el encoder es bidireccional, se suelen concatenar los estados de ambas direcciones, y $\mathbf{c}$ puede ser la concatenación de los últimos estados o una combinación.

### Funcionamiento del Decoder

El decoder genera la secuencia de salida paso a paso, comenzando con un token especial `<sos>` (start of sentence). Su estado inicial se fija con el vector de contexto:

$$ \mathbf{s}_0 = \mathbf{c}. $$

En cada paso $t$:

1. Recibe la palabra generada en el paso anterior $y_{t-1}$ (durante el entrenamiento, se utiliza la palabra verdadera – **teacher forcing**).
2. Actualiza su estado oculto:
   $$ \mathbf{s}_t = \text{RNN}_\text{dec}(\mathbf{e}(y_{t-1}), \mathbf{s}_{t-1}). $$
3. Produce una distribución sobre el vocabulario destino:
   $$ P(y_t \mid y_{<t}, \mathbf{c}) = \text{softmax}(\mathbf{W}_o \mathbf{s}_t + \mathbf{b}_o). $$
4. En inferencia, se elige la palabra más probable o se usa beam search.

La generación continúa hasta emitir el token `<eos>` o alcanzar una longitud máxima.

### Ejemplo de Encoder -  Decoder

Imaginemos que queremos traducir la frase:

> **"I am fine"**

a español. Usaremos un vocabulario muy reducido:

- **Vocabulario fuente (inglés)**: `{"I": 1, "am": 2, "fine": 3, "<sos>": 4, "<eos>": 5}`
- **Vocabulario destino (español)**: `{"Yo": 1, "estoy": 2, "bien": 3, "<sos>": 4, "<eos>": 5}`

Vamos a usar **embeddings** de dimensión 2 (cada palabra se representa como un vector de 2 números). Los **estados ocultos** también tendrán dimensión 2. Elegiremos valores redondos para facilitar las cuentas.

### Parámetros ficticios del modelo

- **Embeddings** (cada palabra se mapea a un vector):

| Palabra | Embedding $\mathbf{e}(\cdot)$ |
|---------|------------------------------|
| "I"     | $[1.0, 0.5]$                 |
| "am"    | $[0.8, 0.7]$                 |
| "fine"  | $[0.2, 0.9]$                 |
| "<sos>" | $[0.0, 0.0]$ (solo para inicio) |

- **Pesos del encoder** (una RNN simple, sin compuertas para simplificar):  
  $$ \mathbf{h}_t = \tanh(\mathbf{W}_{xh} \mathbf{e}(x_t) + \mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{b}_h) $$

  Tomaremos valores inventados:
  $$ \mathbf{W}_{xh} = \begin{bmatrix} 0.5 & 0.2 \\ 0.3 & 0.7 \end{bmatrix}, \quad
     \mathbf{W}_{hh} = \begin{bmatrix} 0.1 & 0.0 \\ 0.0 & 0.1 \end{bmatrix}, \quad
     \mathbf{b}_h = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix} $$

- **Pesos del decoder** (similares, pero con otros valores para distinguir):
  $$ \mathbf{W}_{xh}^{dec} = \begin{bmatrix} 0.6 & 0.1 \\ 0.2 & 0.8 \end{bmatrix}, \quad
     \mathbf{W}_{hh}^{dec} = \begin{bmatrix} 0.1 & 0.0 \\ 0.0 & 0.1 \end{bmatrix}, \quad
     \mathbf{b}_h^{dec} = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix} $$

- **Capa de salida del decoder**:  
  $$ \mathbf{W}_o = \begin{bmatrix} 0.4 & 0.3 \\ 0.2 & 0.5 \\ 0.1 & 0.6 \\ 0.7 & 0.2 \\ 0.3 & 0.4 \end{bmatrix} \quad (\text{5 filas, una por palabra del vocabulario destino}) $$
  $$ \mathbf{b}_o = \begin{bmatrix} 0.0 \\ 0.0 \\ 0.0 \\ 0.0 \\ 0.0 \end{bmatrix} $$

---

## 1. Funcionamiento del Encoder

El encoder leerá la secuencia de entrada **"I am fine"** (tres palabras) y generará tres estados ocultos $\mathbf{h}_1, \mathbf{h}_2, \mathbf{h}_3$. Al final, $\mathbf{h}_3$ será el **vector de contexto** $\mathbf{c}$.

### Paso 1: Inicialización

$\mathbf{h}_0 = [0.0, 0.0]$ (vector de ceros).

### Paso 2: Procesar la primera palabra $x_1 = \text{"I"}$

- Embedding: $\mathbf{e}(\text{"I"}) = [1.0, 0.5]$
- Actualización:
  $$ \mathbf{h}_1 = \tanh\!\left( \mathbf{W}_{xh} \cdot [1.0, 0.5] + \mathbf{W}_{hh} \cdot [0.0, 0.0] + \mathbf{b}_h \right) $$

  Calculamos $\mathbf{W}_{xh} \cdot \mathbf{e}$:
  $$ \begin{bmatrix} 0.5 & 0.2 \\ 0.3 & 0.7 \end{bmatrix} \cdot \begin{bmatrix} 1.0 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 0.5*1.0 + 0.2*0.5 \\ 0.3*1.0 + 0.7*0.5 \end{bmatrix} = \begin{bmatrix} 0.5 + 0.1 \\ 0.3 + 0.35 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.65 \end{bmatrix} $$

  Como $\mathbf{h}_0 = [0,0]$, el término $\mathbf{W}_{hh}\mathbf{h}_0$ es $[0,0]$.

  Sumamos $\mathbf{b}_h = [0,0]$, obtenemos $[0.6, 0.65]$. Aplicamos $\tanh$ (recordemos que $\tanh(x)$ mapea a valores entre -1 y 1; para estos números, valores aproximados):
  - $\tanh(0.6) \approx 0.537$
  - $\tanh(0.65) \approx 0.571$

  Por tanto, $\mathbf{h}_1 \approx [0.537, 0.571]$.

### Paso 3: Procesar la segunda palabra $x_2 = \text{"am"}$

- Embedding: $\mathbf{e}(\text{"am"}) = [0.8, 0.7]$
- Estado anterior $\mathbf{h}_1 = [0.537, 0.571]$

  Calculamos $\mathbf{W}_{xh} \cdot \mathbf{e}$:
  $$ \begin{bmatrix} 0.5 & 0.2 \\ 0.3 & 0.7 \end{bmatrix} \cdot \begin{bmatrix} 0.8 \\ 0.7 \end{bmatrix} = \begin{bmatrix} 0.5*0.8 + 0.2*0.7 \\ 0.3*0.8 + 0.7*0.7 \end{bmatrix} = \begin{bmatrix} 0.4 + 0.14 \\ 0.24 + 0.49 \end{bmatrix} = \begin{bmatrix} 0.54 \\ 0.73 \end{bmatrix} $$

  Calculamos $\mathbf{W}_{hh} \cdot \mathbf{h}_1$:
  $$ \begin{bmatrix} 0.1 & 0.0 \\ 0.0 & 0.1 \end{bmatrix} \cdot \begin{bmatrix} 0.537 \\ 0.571 \end{bmatrix} = \begin{bmatrix} 0.1*0.537 + 0.0*0.571 \\ 0.0*0.537 + 0.1*0.571 \end{bmatrix} = \begin{bmatrix} 0.0537 \\ 0.0571 \end{bmatrix} $$

  Sumamos: $[0.54+0.0537, \ 0.73+0.0571] = [0.5937, 0.7871]$

  Aplicamos $\tanh$:
  - $\tanh(0.5937) \approx 0.533$
  - $\tanh(0.7871) \approx 0.656$

  Por tanto, $\mathbf{h}_2 \approx [0.533, 0.656]$.

### Paso 4: Procesar la tercera palabra $x_3 = \text{"fine"}$

- Embedding: $\mathbf{e}(\text{"fine"}) = [0.2, 0.9]$
- Estado anterior $\mathbf{h}_2 = [0.533, 0.656]$

  $\mathbf{W}_{xh} \cdot \mathbf{e}$:
  $$ \begin{bmatrix} 0.5 & 0.2 \\ 0.3 & 0.7 \end{bmatrix} \cdot \begin{bmatrix} 0.2 \\ 0.9 \end{bmatrix} = \begin{bmatrix} 0.5*0.2 + 0.2*0.9 \\ 0.3*0.2 + 0.7*0.9 \end{bmatrix} = \begin{bmatrix} 0.1 + 0.18 \\ 0.06 + 0.63 \end{bmatrix} = \begin{bmatrix} 0.28 \\ 0.69 \end{bmatrix} $$

  $\mathbf{W}_{hh} \cdot \mathbf{h}_2$:
  $$ \begin{bmatrix} 0.1 & 0.0 \\ 0.0 & 0.1 \end{bmatrix} \cdot \begin{bmatrix} 0.533 \\ 0.656 \end{bmatrix} = \begin{bmatrix} 0.0533 \\ 0.0656 \end{bmatrix} $$

  Suma: $[0.28+0.0533, \ 0.69+0.0656] = [0.3333, 0.7556]$

  $\tanh(0.3333) \approx 0.322$  
  $\tanh(0.7556) \approx 0.637$

  Por tanto, $\mathbf{h}_3 \approx [0.322, 0.637]$.

### Resultado final del encoder

Los estados ocultos son:
- $\mathbf{h}_1 = [0.537, 0.571]$
- $\mathbf{h}_2 = [0.533, 0.656]$
- $\mathbf{h}_3 = [0.322, 0.637]$

El **vector de contexto** $\mathbf{c}$ es el último estado: $\mathbf{c} = \mathbf{h}_3 = [0.322, 0.637]$. Este vector se pasará al decoder como estado inicial.

---

## 2. Funcionamiento del Decoder

El decoder generará la salida palabra por palabra. Comienza con el token `<sos>` (cuyo embedding es $[0,0]$) y el estado inicial $\mathbf{s}_0 = \mathbf{c} = [0.322, 0.637]$.

### Paso 1: Generar la primera palabra de salida ($t=1$)

- Entrada al decoder: $y_0 = \text{"<sos>"}$ (token especial de inicio).
- Embedding: $\mathbf{e}(\text{"<sos>"}) = [0.0, 0.0]$.
- Estado anterior: $\mathbf{s}_0 = [0.322, 0.637]$.

Actualizamos el estado del decoder:
$$ \mathbf{s}_1 = \tanh\!\left( \mathbf{W}_{xh}^{dec} \cdot \mathbf{e}(y_0) + \mathbf{W}_{hh}^{dec} \cdot \mathbf{s}_0 + \mathbf{b}_h^{dec} \right) $$

- $\mathbf{W}_{xh}^{dec} \cdot \mathbf{e}(y_0) = \begin{bmatrix} 0.6 & 0.1 \\ 0.2 & 0.8 \end{bmatrix} \cdot [0,0] = [0,0]$.
- $\mathbf{W}_{hh}^{dec} \cdot \mathbf{s}_0 = \begin{bmatrix} 0.1 & 0.0 \\ 0.0 & 0.1 \end{bmatrix} \cdot [0.322, 0.637] = [0.0322, 0.0637]$.
- Suma con $\mathbf{b}_h^{dec}=[0,0]$ → $[0.0322, 0.0637]$.
- $\tanh(0.0322) \approx 0.0322$, $\tanh(0.0637) \approx 0.0636$.

Por tanto, $\mathbf{s}_1 \approx [0.0322, 0.0636]$.

Ahora calculamos la distribución de probabilidad sobre el vocabulario destino:

$$ \mathbf{z} = \mathbf{W}_o \mathbf{s}_1 + \mathbf{b}_o = \mathbf{W}_o \cdot [0.0322, 0.0636] $$

$\mathbf{W}_o$ tiene 5 filas (por las 5 palabras del vocabulario destino). Multiplicamos cada fila:

- Para "Yo" (fila 1): $0.4*0.0322 + 0.3*0.0636 = 0.01288 + 0.01908 = 0.03196$
- Para "estoy" (fila 2): $0.2*0.0322 + 0.5*0.0636 = 0.00644 + 0.0318 = 0.03824$
- Para "bien" (fila 3): $0.1*0.0322 + 0.6*0.0636 = 0.00322 + 0.03816 = 0.04138$
- Para "<sos>" (fila 4): $0.7*0.0322 + 0.2*0.0636 = 0.02254 + 0.01272 = 0.03526$
- Para "<eos>" (fila 5): $0.3*0.0322 + 0.4*0.0636 = 0.00966 + 0.02544 = 0.03510$

Obtenemos $\mathbf{z} = [0.0320, 0.0382, 0.0414, 0.0353, 0.0351]$.  
Luego aplicamos **softmax** para convertirlo en probabilidades:

$$ \text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_j e^{z_j}} $$

Calculamos los exponenciales (valores aproximados):
- $e^{0.0320} \approx 1.0325$
- $e^{0.0382} \approx 1.0389$
- $e^{0.0414} \approx 1.0423$
- $e^{0.0353} \approx 1.0359$
- $e^{0.0351} \approx 1.0357$

Suma total ≈ $1.0325+1.0389+1.0423+1.0359+1.0357 = 5.1853$.

Probabilidades:
- "Yo": $1.0325 / 5.1853 \approx 0.199$
- "estoy": $1.0389 / 5.1853 \approx 0.200$
- "bien": $1.0423 / 5.1853 \approx 0.201$
- "<sos>": $1.0359 / 5.1853 \approx 0.200$
- "<eos>": $1.0357 / 5.1853 \approx 0.200$

La distribución es casi uniforme (por los valores inventados). La palabra más probable es **"bien"** con 0.201. En la práctica, el modelo elegiría "bien" como primera palabra de salida.

### Paso 2: Generar la segunda palabra ($t=2$)

Ahora usamos la palabra generada (o la verdadera durante entrenamiento). Supongamos que hemos elegido $y_1 = \text{"bien"}$. Su embedding: $\mathbf{e}(\text{"bien"}) = $ (necesitaríamos definirlo; pero para este ejemplo usaremos un embedding ficticio: supongamos que es $[0.5, 0.4]$). El estado anterior es $\mathbf{s}_1 = [0.0322, 0.0636]$.

Repetimos el proceso con las mismas matrices, pero con la nueva entrada. No lo desarrollaremos completamente por extensión, pero la idea es la misma: se actualiza $\mathbf{s}_2$ y se calcula otra distribución. El proceso continúa hasta que se genera `<eos>`.

---

## 3. Visualización de las operaciones con números

### Encoder (resumen numérico)

| Paso | Entrada $x_t$ | $\mathbf{e}(x_t)$ | $\mathbf{h}_{t-1}$ | $\mathbf{h}_t$ (después de tanh) |
|------|---------------|-------------------|--------------------|----------------------------------|
| 1    | "I"           | [1.0, 0.5]        | [0.0, 0.0]         | [0.537, 0.571]                  |
| 2    | "am"          | [0.8, 0.7]        | [0.537, 0.571]     | [0.533, 0.656]                  |
| 3    | "fine"        | [0.2, 0.9]        | [0.533, 0.656]     | [0.322, 0.637] ← $\mathbf{c}$   |

### Decoder (primer paso)

| Variable          | Valor                                      |
|-------------------|--------------------------------------------|
| $\mathbf{s}_0$    | [0.322, 0.637]                             |
| Entrada $y_0$     | "<sos>" → $\mathbf{e}=[0,0]$               |
| $\mathbf{s}_1$    | [0.0322, 0.0636]                           |
| $\mathbf{z}$      | [0.0320, 0.0382, 0.0414, 0.0353, 0.0351]  |
| Probabilidades    | [0.199, 0.200, 0.201, 0.200, 0.200]        |
| Palabra elegida   | "bien"                                     |

---

## 4. ¿Por qué son importantes estos números?

- **Embeddings** ($\mathbf{e}(x_t)$): convierten palabras en vectores que el modelo puede procesar numéricamente.
- **Estados ocultos** ($\mathbf{h}_t$): representan el "resumen" de la secuencia hasta el paso $t$. Cada paso agrega información nueva y transforma la anterior.
- **Pesos** ($\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$, etc.): son parámetros que el modelo aprende durante el entrenamiento para realizar las transformaciones.
- **Softmax**: convierte puntuaciones (logits) en una distribución de probabilidad que permite elegir la palabra más probable.

**Recuerda**: Este ejemplo usa números inventados; en la práctica, los valores son el resultado del entrenamiento con muchos datos. La dimensión de los vectores suele ser mucho mayor (256, 512, etc.) y las funciones de activación pueden ser LSTM o GRU en lugar de la RNN simple que usamos aquí, pero la esencia es la misma.




### Limitación del contexto fijo

El vector de contexto $\mathbf{c}$ es una representación de **dimensión fija** que debe capturar toda la información de la entrada. Esto se convierte en un **cuello de botella** cuando la secuencia es larga: la información de las primeras palabras puede perderse o diluirse. Además, diferentes partes de la salida pueden depender de diferentes partes de la entrada, pero $\mathbf{c}$ no puede enfocarse en una región específica.

## Motivación de la atención

La **atención** surge para superar estas limitaciones. En lugar de comprimir toda la entrada en un solo vector, permite que el decodificador, en cada paso de generación, **observe** todos los estados del encoder y decida dinámicamente cuáles son más relevantes. Esto se logra calculando un **vector de contexto dinámico** $\mathbf{c}_t$ que es una suma ponderada de los estados del encoder, donde los pesos reflejan la relevancia de cada palabra de entrada para la palabra que se está generando.

## Mecanismo de Atención

### Introducción

El mecanismo de atención fue introducido en traducción automática por Bahdanau et al. (2015) y posteriormente simplificado por Luong et al. (2015). La idea fundamental es que en el paso $t$ del decodificador, se calcula un conjunto de pesos $\alpha_{t,1}, \dots, \alpha_{t,T}$ sobre los estados del encoder $\mathbf{h}_1, \dots, \mathbf{h}_T$, y se obtiene el contexto como:

$$ \mathbf{c}_t = \sum_{i=1}^T \alpha_{t,i} \mathbf{h}_i. $$

### Cálculo de la atención (score, pesos, contexto)

El cálculo se realiza en tres pasos:

1. **Puntuaciones de alineación (scores)**: Se calcula una puntuación $e_{t,i}$ que mide qué tan bien se alinea el estado del encoder $\mathbf{h}_i$ con el estado actual del decodificador $\mathbf{s}_t$ (o el anterior, según la variante).
2. **Normalización (softmax)**: Se convierten las puntuaciones en una distribución de probabilidad:
   $$ \alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_{j=1}^T \exp(e_{t,j})}. $$
3. **Vector de contexto**: Se pondera cada estado del encoder por su peso y se suman:
   $$ \mathbf{c}_t = \sum_{i=1}^T \alpha_{t,i} \mathbf{h}_i. $$

Luego, $\mathbf{c}_t$ se combina con $\mathbf{s}_t$ para predecir la palabra de salida.

### Dzmitry Bahdanau (Atención Aditiva)

En el trabajo de Bahdanau et al. (2015), la puntuación se calcula usando una red neuronal pequeña (función de alineación aditiva) que toma el estado anterior del decodificador $\mathbf{s}_{t-1}$ y el estado del encoder $\mathbf{h}_i$:

$$ e_{t,i} = \mathbf{v}_a^\top \tanh(\mathbf{W}_a \mathbf{s}_{t-1} + \mathbf{U}_a \mathbf{h}_i), $$

donde $\mathbf{v}_a$, $\mathbf{W}_a$ y $\mathbf{U}_a$ son parámetros aprendibles. Una vez obtenido $\mathbf{c}_t$, se concatena con $\mathbf{s}_{t-1}$ y se pasa por una capa lineal para actualizar el estado del decodificador antes de la predicción.

### Minh-Thang Luong (Atención Multiplicativa)

Luong et al. (2015) proponen una formulación más eficiente que utiliza el estado **actual** del decodificador $\mathbf{s}_t$ (después de procesar la palabra de entrada) para calcular los scores. Ofrecen tres opciones:

- **Producto punto (dot)**: $e_{t,i} = \mathbf{s}_t^\top \mathbf{h}_i$.
- **Producto general (general)**: $e_{t,i} = \mathbf{s}_t^\top \mathbf{W}_a \mathbf{h}_i$, con $\mathbf{W}_a$ aprendible.
- **Concat**: $e_{t,i} = \mathbf{v}_a^\top \tanh(\mathbf{W}_a [\mathbf{s}_t; \mathbf{h}_i])$ (similar a Bahdanau pero con $\mathbf{s}_t$).

El contexto $\mathbf{c}_t$ se calcula igual y luego se combina con $\mathbf{s}_t$ para la predicción final. Esta variante es más simple y computacionalmente más liviana.

### Atención global vs. local

Luong et al. también introducen la distinción:

- **Atención global**: se consideran **todos** los estados del encoder para calcular $\mathbf{c}_t$. Es la forma más común y captura toda la información, pero su costo computacional es $O(T)$ por paso de decodificación.
- **Atención local**: se predice primero una posición alineada $p_t$ en la entrada (por ejemplo, mediante una red que mira el estado actual) y luego se calcula la atención solo sobre una ventana de tamaño fijo alrededor de $p_t$. Esto reduce la complejidad a $O(\text{ventana})$ y es útil para secuencias muy largas.

## Resumen

- Los modelos **Seq2Seq** con arquitectura encoder-decoder permiten transformar secuencias de longitud variable, pero el vector de contexto fijo es un cuello de botella.
- El **mecanismo de atención** resuelve este problema permitiendo al decodificador enfocarse dinámicamente en diferentes partes de la entrada en cada paso.
- Existen dos formulaciones principales:
  - **Bahdanau (aditiva)**: usa el estado anterior del decodificador $\mathbf{s}_{t-1}$ y una red neuronal para calcular los pesos.
  - **Luong (multiplicativa)**: usa el estado actual $\mathbf{s}_t$ y ofrece variantes de producto punto o producto general.
- La atención puede ser **global** (toda la entrada) o **local** (ventana), balanceando precisión y eficiencia.
- Estos conceptos son la base de arquitecturas más modernas como los **Transformers**, donde la atención es el componente central.