# main.py

from config.settings import ACTIVATION_WORD
from core.voice_input import listen_for_activation, capture_user_query
from core.voice_output import speak
from core.llm_integration import ask_llm
from core.task_handler import handle_task
from database.database import initialize_database, save_interaction

def main():
    """
    Punto de entrada principal del asistente Yarvis.
    - Escucha comandos de voz.
    - Procesa consultas generales o tareas específicas.
    - Responde en voz.
    """
    print("Inicializando Yarvis...")
    speak("Hola, soy Yarvis. Estoy listo para ayudarte.")
    initialize_database()  # Asegurarse de que la base de datos está configurada.

    while True:
        # Escuchar activación
        command = listen_for_activation()
        if ACTIVATION_WORD in command:
            speak("¡Yarvis activado! ¿En qué puedo ayudarte?")
            
            # Capturar la consulta del usuario
            user_query = capture_user_query()
            if not user_query:
                speak("Lo siento, no entendí tu consulta.")
                continue
            
            # Procesar la consulta: General o Específica
            if "pedido" in user_query or "cita" in user_query:
                response = handle_task(user_query)
            else:
                response = ask_llm(user_query)

            # Responder al usuario
            speak(response)

            # Guardar interacción en la base de datos
            save_interaction(user_query, response)

if __name__ == "__main__":
    main()
