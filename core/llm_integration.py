import openai
from config.settings import OPENAI_API_KEY

def ask_llm(prompt):
    """
    Envía un prompt a ChatGPT y devuelve la respuesta generada.

    Args:
        prompt (str): Consulta del usuario en texto.

    Returns:
        str: Respuesta generada por el modelo de lenguaje.
    """
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error al conectarse con ChatGPT: {e}"
