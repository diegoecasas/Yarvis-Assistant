import speech_recognition as sr
from config.settings import LANGUAGE, ACTIVATION_WORD

def listen_for_activation():
    """
    Escucha continuamente al usuario hasta detectar la palabra de activación.
    Retorna el comando completo dicho por el usuario o una cadena vacía si no se detecta.
    """
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language=LANGUAGE).lower()
                if ACTIVATION_WORD in command:
                    return command
            except sr.UnknownValueError:
                continue  # Ignorar ruido o comandos no entendidos
            except sr.RequestError:
                return ""  # Error al conectarse al servicio de reconocimiento

def capture_user_query():
    """
    Captura la consulta del usuario tras la activación.
    Retorna la consulta como texto o una cadena vacía si no se detecta entrada clara.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language=LANGUAGE).lower()
            return query
        except sr.UnknownValueError:
            return ""  # No se entendió la consulta
        except sr.RequestError:
            return ""  # Error al conectarse al servicio de reconocimiento
