import re
import random

# 1. DICCIONARIO DE REFLEXIÓN
# Cambia los pronombres del usuario para que el bot responda desde su perspectiva
reflexiones = {
    "yo": "tú",
    "mi": "tu",
    "me": "te",
    "soy": "eres",
    "estoy": "estás",
    "mío": "tuyo"
}

# 2. PATRONES Y RESPUESTAS
# Una lista de tuplas: (Expresión Regular, [Lista de posibles respuestas])
patrones = [
    (r'necesito (.*)',
     ["¿Por qué necesitas {0}?",
      "¿Realmente te ayudaría conseguir {0}?",
      "¿Estás seguro de que necesitas {0}?"]),
    
    (r'por qué no puedes (.*)',
     ["¿Crees que debería poder {0}?",
      "Si pudiera {0}, ¿qué harías?",
      "No sé si puedo {0}."]),
    
    (r'siento (.*)',
     ["Cuéntame más sobre esos sentimientos.",
      "¿A menudo te sientes {0}?",
      "¿Cuándo sueles sentirte {0}?"]),
    
    (r'mi madre (.*)|mi papá (.*)|mi familia (.*)',
     ["Háblame más sobre tu familia.",
      "¿Cómo es tu relación con ellos?",
      "¿Qué te hace pensar en tu familia ahora?"]),
    
    (r'estoy (.*)',
     ["¿Por qué crees que estás {0}?",
      "¿Te gusta estar {0}?",
      "¿Qué te hizo estar {0}?"]),
    
    (r'hola(.*)',
     ["¡Hola! ¿De qué te gustaría hablar hoy?",
      "Hola. ¿Cómo te sientes en este momento?"]),
    
    (r'adios(.*)|chao(.*)',
     ["Gracias por hablar conmigo. ¡Hasta pronto!",
      "Adiós. Espero que te sientas mejor."]),
    
    # PATRÓN DE RESPALDO (Fallback) si no entiende nada
    (r'(.*)',
     ["Cuéntame más.",
      "Entiendo. Continúa, por favor.",
      "¿Cómo te hace sentir eso?",
      "Muy interesante...",
      "¿Puedes elaborar un poco más sobre eso?"])
]

def reflejar_pronombres(texto):
    """Reemplaza los pronombres del texto usando el diccionario."""
    palabras = texto.lower().split()
    for i, palabra in enumerate(palabras):
        if palabra in reflexiones:
            palabras[i] = reflexiones[palabra]
    return ' '.join(palabras)

def eliza_responde(entrada_usuario):
    """Busca un patrón que coincida con la entrada del usuario y genera la respuesta."""
    for patron, respuestas in patrones:
        coincidencia = re.match(patron, entrada_usuario.lower().rstrip(".!?,;"))
        
        if coincidencia:
            # Elige una respuesta aleatoria de la lista disponible
            respuesta_elegida = random.choice(respuestas)
            
            # Si el patrón capturó grupos ((.*)), los reflejamos e insertamos
            if '{0}' in respuesta_elegida:
                grupo_capturado = coincidencia.groups()[0]
                frase_reflejada = reflejar_pronombres(grupo_capturado)
                return respuesta_elegida.format(frase_reflejada)
            else:
                return respuesta_elegida

def iniciar_terapia():
    print("ELIZA: Hola, soy Eliza, tu psicoterapeuta virtual. (Escribe 'adios' para salir)")
    print("-" * 50)
    
    while True:
        entrada = input("TÚ: ")
        if re.match(r'adios|chao|salir', entrada.lower()):
            print("ELIZA: " + random.choice(patrones[6][1]))
            break
        
        respuesta = eliza_responde(entrada)
        print("ELIZA: " + respuesta)

# Ejecutar el programa
if __name__ == "__main__":
    iniciar_terapia()