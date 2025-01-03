import unittest
from unittest.mock import patch, MagicMock
from core.voice_input import listen_for_activation, capture_user_query
from core.voice_output import speak

class TestVoiceModule(unittest.TestCase):

    @patch('core.voice_input.sr.Recognizer.listen')
    @patch('core.voice_input.sr.Recognizer.recognize_google')
    def test_listen_for_activation(self, mock_recognize, mock_listen):
        """Prueba que listen_for_activation detecte la palabra clave."""
        mock_recognize.return_value = "yarvis hola"
        result = listen_for_activation()
        self.assertIn("yarvis", result)

    @patch('core.voice_input.sr.Recognizer.listen')
    @patch('core.voice_input.sr.Recognizer.recognize_google')
    def test_capture_user_query(self, mock_recognize, mock_listen):
        """Prueba que capture_user_query convierta voz en texto correctamente."""
        mock_recognize.return_value = "quiero saber el clima"
        result = capture_user_query()
        self.assertEqual(result, "quiero saber el clima")

    @patch('core.voice_output.initialize_voice')
    def test_speak(self, mock_initialize_voice):
        """Prueba que speak invoque el motor de texto a voz correctamente."""
        mock_engine = MagicMock()
        mock_initialize_voice.return_value = mock_engine
        speak("Hola")
        mock_engine.say.assert_called_with("Hola")
        mock_engine.runAndWait.assert_called()

if __name__ == "__main__":
    unittest.main()
