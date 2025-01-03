# Yarvis: Asistente Virtual por Voz

**Yarvis** es un asistente virtual de voz que integra tecnologías avanzadas como ChatGPT, entrada y salida de voz, y una interfaz visual opcional. Este prototipo inicial está diseñado para evolucionar hacia un producto comercial basado en suscripciones.

---

## Características

1. **Activación por voz:**
   - Detecta la palabra clave "Yarvis" para activarse.

2. **Respuestas inteligentes:**
   - Integra un modelo de lenguaje como ChatGPT para responder preguntas y gestionar tareas.

3. **Salida de voz:**
   - Convierte respuestas generadas en texto a voz para una interacción fluida y natural.

4. **Registro de interacciones:**
   - Guarda consultas y respuestas en una base de datos SQLite.

5. **Interfaz visual opcional:**
   - Proporciona una pantalla oscura con línea oscilante para indicar actividad.

---

## Arquitectura

La arquitectura modular de Yarvis garantiza escalabilidad y facilidad de mantenimiento. Aquí está la representación gráfica y su explicación.

### **Gráfica de la Arquitectura**

![Arquitectura de Yarvis](path/to/architecture-image.png)

### **Explicación**

1. **`main.py`**:
   - Coordina el flujo del asistente desde la activación por voz hasta la respuesta hablada.

2. **`config/`**:
   - Configuraciones globales (claves API, rutas, valores compartidos).

3. **`core/`**:
   - Lógica principal del asistente:
     - Captura de voz.
     - Conversión de texto a voz.
     - Comunicación con ChatGPT.

4. **`ui/`**:
   - Pantalla oscura opcional con línea oscilante que indica actividad.

5. **`database/`**:
   - Gestión de interacciones y datos de usuario mediante SQLite.

6. **`utils/`**:
   - Funciones auxiliares y manejo de logs.

7. **`tests/`**:
   - Pruebas unitarias de cada componente.

---

## Instalación

### Requisitos

- **Python 3.8 o superior.**
- Instalar las dependencias desde el archivo `requirements.txt`.

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/yarvis.git
   cd yarvis
   ```

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar las claves de API:**
   - Editar `config/settings.py` y añadir la clave de OpenAI.

4. **Inicializar la base de datos:**
   ```bash
   sqlite3 database/yarvis.db < database/schema.sql
   ```

5. **Ejecutar el asistente:**
   ```bash
   python main.py
   ```

---

## Estructura del Proyecto

```plaintext
yarvis_assistant/
│
├── main.py                # Coordina el flujo principal del asistente.
├── config/
│   ├── settings.py         # Configuración básica.
│   ├── constants.py        # Constantes compartidas.
│
├── core/                  # Lógica principal.
│   ├── voice_input.py      # Captura de entrada de voz.
│   ├── voice_output.py     # Conversión de texto a voz.
│   ├── llm_integration.py  # Comunicación con ChatGPT.
│
├── ui/                    # Interfaz visual.
│   ├── dark_ui.py          # Pantalla oscura con línea oscilante.
│
├── database/              # Gestión de base de datos.
│   ├── database.py         # Interacciones y usuarios.
│   └── schema.sql          # Esquema inicial.
│
├── utils/                 # Funciones auxiliares y logs.
│   ├── logger.py           # Manejo de registros.
│   ├── helpers.py          # Funciones comunes.
│
├── tests/                 # Pruebas unitarias.
│   ├── test_voice.py       # Pruebas de entrada y salida de voz.
│   ├── test_llm.py         # Pruebas de integración con ChatGPT.
│   ├── test_database.py    # Pruebas de base de datos.
│
├── README.md               # Documentación.
├── LICENSE                 # Licencia de uso.
└── requirements.txt        # Dependencias.
```

---

## Contribuciones

1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios.
3. Realiza un pull request describiendo las modificaciones.

---

## Licencia

Este proyecto está bajo una licencia comercial exclusiva, administrada por GRUPO CASAS SAS. Consulta el archivo `LICENSE` para más información.
