import unittest
from unittest.mock import patch
from core.llm_integration import ask_llm

class TestLLMIntegration(unittest.TestCase):

    @patch('core.llm_integration.openai.ChatCompletion.create')
    def test_ask_llm_success(self, mock_chat_completion):
        """Prueba que ask_llm devuelva la respuesta esperada del modelo."""
        # Configurar el mock para devolver una respuesta simulada
        mock_chat_completion.return_value = {
            "choices": [{"message": {"content": "Respuesta simulada"}}]
        }

        # Llamar a la función
        response = ask_llm("¿Cuál es la capital de Francia?")

        # Verificar que la respuesta sea correcta
        self.assertEqual(response, "Respuesta simulada")

    @patch('core.llm_integration.openai.ChatCompletion.create')
    def test_ask_llm_error(self, mock_chat_completion):
        """Prueba que ask_llm maneje errores correctamente."""
        # Configurar el mock para lanzar una excepción
        mock_chat_completion.side_effect = Exception("Error de conexión")

        # Llamar a la función
        response = ask_llm("¿Cuál es la capital de Francia?")

        # Verificar que se devuelva un mensaje de error
        self.assertIn("Error al conectarse", response)

if __name__ == "__main__":
    unittest.main()
