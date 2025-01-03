import pyttsx3
from config.constants import ERROR_MESSAGE

def initialize_voice():
    """Inicializa el motor de texto a voz y configura sus propiedades."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de la voz
    engine.setProperty('volume', 1.0)  # Volumen máximo
    voices = engine.getProperty('voices')
    # Configurar a español si está disponible
    for voice in voices:
        if "es" in voice.id:
            engine.setProperty('voice', voice.id)
            break
    return engine

def speak(text):
    """Convierte texto en voz y lo reproduce."""
    try:
        engine = initialize_voice()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        fallback_error_handling(e)

def fallback_error_handling(error):
    """Manejo de errores para salida de voz."""
    print(f"Error en la síntesis de voz: {error}")
    engine = initialize_voice()
    engine.say(ERROR_MESSAGE.format(user_name="usuario"))
    engine.runAndWait()
    engine.stop()
