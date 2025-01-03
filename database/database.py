import sqlite3
from config.constants import DATABASE_PATH

def initialize_database():
    """
    Inicializa la base de datos SQLite creando las tablas necesarias si no existen.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Crear tabla para interacciones
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT NOT NULL,
            response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # Crear tabla para información del usuario
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
    )

    # Insertar un usuario por defecto si no existe
    cursor.execute(
        """
        INSERT INTO user (name)
        SELECT 'Usuario' WHERE NOT EXISTS (SELECT 1 FROM user)
        """
    )

    conn.commit()
    conn.close()

def save_interaction(user_input, response):
    """
    Guarda una interacción entre el usuario y Yarvis en la base de datos.

    Args:
        user_input (str): Texto ingresado por el usuario.
        response (str): Respuesta generada por Yarvis.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO interactions (user_input, response) VALUES (?, ?)",
        (user_input, response)
    )

    conn.commit()
    conn.close()

def get_user_name():
    """
    Obtiene el nombre del usuario desde la base de datos.

    Returns:
        str: Nombre del usuario.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM user LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else "Usuario"
