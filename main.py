# main.py
from core.voice_input import listen_for_activation, capture_user_query
from core.voice_output import speak
from config.settings import ACTIVATION_WORD
from database.database import get_user_name

def main():
    """
    Función principal que coordina el flujo del asistente Yarvis.
    - Escucha la palabra de activación.
    - Captura consultas del usuario.
    - Conecta directamente con ChatGPT para obtener respuestas.
    - Responde al usuario mediante voz.
    """
    user_name = get_user_name()  # Obtener el nombre del usuario desde la base de datos
    speak(f"Hola, {user_name}. Soy Yarvis. Estoy listo para ayudarte.")

    while True:
        # Escuchar activación
        command = listen_for_activation()
        if ACTIVATION_WORD in command:
            # Capturar consulta del usuario y procesarla
            user_query = capture_user_query()
            if user_query:
                speak(f"Procesando tu solicitud, {user_name}.")
            else:
                speak(f"No entendí tu consulta, {user_name}. Intenta nuevamente.")

if __name__ == "__main__":
    main()
