---
layout: default
---
# Sesión 3: Modelos Estadísticos y Probabilísticos

### 1. Logro de la sesión

Entender el marco probabilístico clásico de NLP mediante n-gramas, Naive Bayes y técnicas de suavizado.

---

### 2. Marco y alcance

Esta sesión combina teoría, formalización matemática y decisiones de ingeniería para construir soluciones NLP robustas y reproducibles.

| Dimensión | Pregunta guía | Entregable esperado |
|---|---|---|
| Lingüística | ¿Qué fenómeno modelamos? | Definición operativa del problema |
| Estadística | ¿Qué objetivo y supuestos usamos? | Modelo con límites explícitos |
| Ingeniería | ¿Cómo aseguramos reproducibilidad? | Pipeline versionado y trazable |
| Producto | ¿Qué error es tolerable? | Métricas y SLA alineados |

---

### 3. Fundamentos conceptuales

#### 3.1 Regla de Bayes

Permite invertir probabilidades y construir clasificadores generativos interpretables.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.2 Modelo n-grama

Aproxima dependencia larga por contexto local de orden n.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.3 Sparsity en lenguaje

La mayoría de secuencias posibles no se observan en corpus finitos.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.4 Suavizado Laplace

Evita probabilidad cero añadiendo pseudo-conteos.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.5 Good-Turing y Kneser-Ney

Reasignan masa de probabilidad hacia eventos raros/no vistos.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.6 Naive Bayes multinomial

Baseline robusto para texto disperso y pocos datos.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.7 Generativo vs discriminativo

Diferencia entre modelar p(x,y) y p(y|x).

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

#### 3.8 Perplejidad

Medida estándar para calidad de modelo de lenguaje probabilístico.

Implicaciones prácticas:
- Decisión de diseño que habilita este concepto.
- Riesgo si el supuesto central no se cumple.
- Señal observable para validar funcionamiento en datos reales.

---

### 4. Fundamentos matemáticos

Probabilidad de secuencia:

$$P(w_{1:n}) = \prod_{t=1}^{n} P(w_t \mid w_{1:t-1})$$

Objetivo de entrenamiento regularizado:

$$\min_{\theta} \frac{1}{N}\sum_{i=1}^{N}\mathcal{L}(f_\theta(x_i), y_i) + \lambda\,\Omega(\theta)$$

Entropía cruzada multiclase:

$$\mathcal{L}_{CE} = -\sum_{c=1}^{C} y_c\log(\hat{y}_c)$$

Perplejidad:

$$PP = \exp\left(-\frac{1}{N}\sum_{t=1}^{N}\log P(w_t\mid w_{<t})\right)$$

Relación sesgo-varianza (forma conceptual):

$$Error_{gen} = Error_{train} + Error_{complejidad}$$

---

### 5. Historia y protagonistas

NLP moderno es acumulativo: avances teóricos, de cómputo y de evaluación.

| Investigador/a | Contribución relacionada | Lectura en esta sesión |
|---|---|---|
| Thomas Bayes | Base conceptual de inferencia bayesiana. | Referente para contextualizar decisiones metodológicas actuales |
| Frederick Jelinek | Impulso a enfoques estadísticos en reconocimiento del habla. | Referente para contextualizar decisiones metodológicas actuales |
| Stanley Chen | Análisis empírico de smoothing en n-gramas. | Referente para contextualizar decisiones metodológicas actuales |
| Joshua Goodman | Comparativas rigurosas de técnicas probabilísticas. | Referente para contextualizar decisiones metodológicas actuales |

Línea temporal breve:
- 1950-1980: bases simbólicas y probabilísticas.
- 1980-2010: consolidación estadística y modelos clásicos.
- 2010-2017: embeddings distribuidos y deep learning.
- 2017-actualidad: transformers, eficiencia y gobernanza.

---

### 6. Metodología y pipeline

#### 6.1 Definir caso de uso y variable objetivo.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.2 Establecer corpus y criterios de calidad.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.3 Diseñar preprocesamiento reproducible.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.4 Construir baseline interpretable.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.5 Entrenar modelo principal de sesión.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.6 Validar con métricas técnicas y de negocio.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.7 Analizar errores críticos.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

#### 6.8 Planificar despliegue y monitoreo.

Control mínimo de calidad:
- Registrar versión de datos y configuración.
- Separar estrictamente train/valid/test.
- Medir una métrica de proceso y una de resultado.
- Documentar decisiones para mantenimiento futuro.

---

### 7. Evaluación y validación

| Escenario | Métricas sugeridas | Criterio de interpretación |
|---|---|---|
| Clasificación | F1 macro, precisión, recall | Evitar depender solo de accuracy |
| Etiquetado secuencial | F1 por clase/entidad | Reportar clases raras por separado |
| Generación | BLEU/ROUGE + evaluación humana | Fluidez no garantiza fidelidad factual |
| Operación | Latencia p95, throughput, costo | Score alto sin SLA no es suficiente |

Principios de evaluación:
- Desagregar métricas por segmento crítico.
- Comparar solo con protocolos equivalentes.
- Combinar evidencia cuantitativa y cualitativa.
- Conectar métricas con decisiones de despliegue.

---

### 8. Casos aplicados y decisiones de producto

#### 8.1 Atención al cliente e intención

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

#### 8.2 Extracción de entidades en documentos

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

#### 8.3 Resumen y control de factualidad

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

#### 8.4 Búsqueda semántica y recuperación

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

#### 8.5 Moderación de contenido

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

#### 8.6 Asistentes internos con trazabilidad

Checklist de despliegue:
- Definir umbral para automatizar vs escalar a humano.
- Instrumentar observabilidad técnica y de negocio.
- Diseñar estrategia de rollback.
- Revisar cumplimiento legal y privacidad.

---

### 9. Implementación orientativa en Python

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score

df = pd.DataFrame({
    "texto": ["consulta urgente", "mensaje informativo", "reclamo de servicio", "agradecimiento"],
    "label": [1, 0, 1, 0],
})

X_train, X_test, y_train, y_test = train_test_split(
    df["texto"], df["label"], test_size=0.5, random_state=42, stratify=df["label"]
)

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000)),
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print("F1:", f1_score(y_test, pred, zero_division=0))
```

---

### 10. Glosario técnico mínimo

- **Corpus:** Colección de textos usada para análisis y entrenamiento.
- **Token:** Unidad elemental que consume el modelo.
- **Vocabulario:** Conjunto de tokens válidos según tokenizador.
- **OOV:** Términos fuera de vocabulario observado.
- **Data leakage:** Fuga de información entre etapas de evaluación.
- **Drift:** Cambio de distribución en datos o etiquetas.
- **Latencia p95:** Percentil operativo de tiempo de respuesta.
- **Guardrail:** Regla de seguridad en entrada/salida del sistema.

---

## Referencias bibliográficas principales

1. Jurafsky, D., & Martin, J. H. *Speech and Language Processing*.
2. Manning, C., Raghavan, P., & Schutze, H. *Introduction to Information Retrieval*.
3. Eisenstein, J. *Introduction to Natural Language Processing*.
4. Goldberg, Y. *Neural Network Methods for NLP*.
5. Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*.
6. Vaswani, A., et al. (2017). Attention Is All You Need.
7. Devlin, J., et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers.
8. Raffel, C., et al. (2020). Exploring the Limits of Transfer Learning with T5.
9. Hu, E., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models.
10. Conneau, A., et al. (2020). Cross-lingual Representation Learning at Scale.
