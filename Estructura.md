yarvis_assistant/
│
├── main.py                # Archivo principal que inicia el asistente.
├── config/
│   ├── settings.py         # Configuración general (API keys, etc.).
│   ├── constants.py        # Constantes y valores compartidos.
│
├── core/
│   ├── voice_input.py      # Captura y procesamiento de entrada de voz.
│   ├── voice_output.py     # Generación y reproducción de salida de voz.
│   ├── llm_integration.py  # Comunicación con ChatGPT u otros LLMs.
│   ├── task_handler.py     # Gestión de tareas como pedidos o citas.
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
