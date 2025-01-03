from core.voice_output import speak
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
                    speak("¡Yarvis activado! ¿En qué puedo ayudarte?")
                    return command
            except sr.UnknownValueError:
                continue  # Ignorar ruido o comandos no entendidos
            except sr.RequestError:
                speak("Error al conectarse al servicio de reconocimiento de voz.")
                return ""

def capture_user_query():
    """
    Captura la consulta del usuario tras la activación.
    Retorna la consulta como texto o una cadena vacía si no se detecta entrada clara.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Estoy escuchando tu consulta.")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language=LANGUAGE).lower()
            return query
        except sr.UnknownValueError:
            speak("Lo siento, no entendí tu consulta.")
            return ""
        except sr.RequestError:
            speak("Error al conectarse al servicio de reconocimiento de voz.")
            return ""