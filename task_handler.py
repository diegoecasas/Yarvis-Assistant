from core.llm_integration import ask_llm
from core.voice_output import speak

def handle_task(user_query):
    """
    Procesa tareas específicas basadas en la consulta del usuario.
    Detecta el contexto (domicilio, cita médica, etc.) y responde apropiadamente.
    
    Args:
        user_query (str): Consulta ingresada por el usuario.

    Returns:
        str: Respuesta procesada para la tarea.
    """
    # Detectar el tipo de tarea
    if "pedido" in user_query:
        task_type = "pedido a domicilio"
        speak("Entendido, procesando tu pedido a domicilio.")
        response = ask_llm(f"Gestiona un {task_type} con la siguiente solicitud: {user_query}")
    elif "cita" in user_query:
        task_type = "cita médica"
        speak("Entendido, procesando tu cita médica.")
        response = ask_llm(f"Gestiona una {task_type} con la siguiente solicitud: {user_query}")
    else:
        task_type = "consulta general"
        speak("Estoy buscando la información para tu consulta.")
        response = ask_llm(user_query)

    # Confirmar la respuesta al usuario
    speak("Aquí está el resultado de tu solicitud.")
    return response
