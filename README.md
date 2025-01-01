# Yarvis: Asistente Virtual por Voz

**Yarvis** es un asistente virtual que interactúa completamente por voz. Diseñado para ser activado mediante la palabra clave "Yarvis", este asistente puede responder preguntas generales, gestionar tareas como pedidos y citas, y registrar todas las interacciones en una base de datos. Yarvis utiliza tecnologías como ChatGPT para generar respuestas inteligentes y un sistema de texto a voz para la comunicación fluida.

---

## Características

1. **Activación por voz:**
   - Detecta la palabra clave "Yarvis" para activarse.

2. **Respuestas inteligentes:**
   - Integra un modelo de lenguaje grande (LLM) como ChatGPT para responder preguntas generales.

3. **Gestión de tareas:**
   - Permite manejar pedidos y citas específicas conectándose con servicios externos como WhatsApp.

4. **Salida de voz:**
   - Convierte respuestas generadas en voz usando tecnologías como `pyttsx3` o `gTTS`.

5. **Registro de interacciones:**
   - Guarda todas las consultas y respuestas en una base de datos SQLite para análisis y auditoría.

---
## Arquitectura del Sistema
![image](https://github.com/user-attachments/assets/5c71cb89-144c-47d6-b12d-d029fb21c155)

---
## Requisitos del Sistema

- Python 3.8 o superior
- Bibliotecas requeridas (ver `requirements.txt`):
  - `speechrecognition`
  - `pyttsx3`
  - `openai`
  - `sqlite3`
  - `pytest` (opcional para pruebas)

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/yarvis.git
   cd yarvis
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las claves de API:**
   - Abre `config/settings.py` y añade tu clave de API de OpenAI:
     ```python
     OPENAI_API_KEY = "tu_clave_api_aqui"
     ```

4. **Ejecuta el asistente:**
   ```bash
   python main.py
   ```

---

## Uso

1. Ejecuta `main.py`.
2. Di la palabra "Yarvis" para activar el asistente.
3. Formula una pregunta o realiza una solicitud:
   - Ejemplo de pregunta general: "Yarvis, ¿cuál es la capital de España?"
   - Ejemplo de solicitud: "Yarvis, agenda una cita médica."
4. Escucha la respuesta hablada y recibe confirmación de las tareas realizadas.

---

## Estructura del Proyecto

```plaintext
yarvis_assistant/
|
├── main.py                # Archivo principal que inicia el asistente.
├── config/
│   ├── settings.py         # Configuración general (API keys, etc.).
│   ├── constants.py        # Constantes y valores compartidos.
│
├── core/
│   ├── voice_input.py      # Captura y procesamiento de entrada de voz.
│   ├── voice_output.py     # Generación y reproducción de salida de voz.
│   ├── llm_integration.py  # Comunicación con ChatGPT u otros LLMs.
│   ├── task_handler.py     # Gestión de tareas como pedidos y citas.
│
├── database/
│   ├── database.py         # Conexión y operaciones con SQLite.
│   └── schema.sql          # Esquema inicial de la base de datos.
│
├── utils/
│   ├── logger.py           # Registro de eventos y depuración.
│   ├── helpers.py          # Funciones auxiliares comunes.
│
├── tests/
│   ├── test_voice.py       # Pruebas para entrada y salida de voz.
│   ├── test_llm.py         # Pruebas para la integración con LLM.
│   ├── test_database.py    # Pruebas para el almacenamiento en SQLite.
│
├── README.md               # Documentación del proyecto.
└── requirements.txt        # Dependencias necesarias (bibliotecas de Python).
```

---

## Próximos Pasos

- **Integración de WhatsApp:** Permitir pedidos y citas médicas mediante WhatsApp.
- **Interfaz de usuario visual:** Crear una representación gráfica para mostrar las interacciones.
- **Soporte para múltiples usuarios:** Ampliar el asistente para gestionar varios perfiles.

---

## Contribuciones

1. Crea un fork del repositorio.
2. Realiza los cambios en una rama separada.
3. Haz un pull request describiendo los cambios.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

