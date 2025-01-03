-- schema.sql

-- Tabla para registrar las interacciones entre el usuario y Yarvis
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para almacenar la información del usuario
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Inserta un usuario por defecto si no existe ningún registro
INSERT INTO user (name)
SELECT 'Usuario'
WHERE NOT EXISTS (SELECT 1 FROM user);
