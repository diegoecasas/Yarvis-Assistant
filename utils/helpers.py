def clean_text(text):
    """
    Limpia y normaliza un texto eliminando caracteres no deseados y espacios extra.

    Args:
        text (str): Texto a limpiar.

    Returns:
        str: Texto limpio y normalizado.
    """
    return ' '.join(text.split()).strip()

def format_response(response, user_name):
    """
    Formatea una respuesta personalizada para el usuario.

    Args:
        response (str): Respuesta original del modelo.
        user_name (str): Nombre del usuario.

    Returns:
        str: Respuesta formateada con el nombre del usuario.
    """
    return response.replace("{user_name}", user_name)

def validate_api_key(api_key):
    """
    Valida si una clave de API es válida.

    Args:
        api_key (str): Clave de API a validar.

    Returns:
        bool: Verdadero si la clave es válida, Falso de lo contrario.
    """
    return isinstance(api_key, str) and len(api_key) > 0
