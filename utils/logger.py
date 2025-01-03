import logging
from config.constants import LOG_FILE_PATH

def initialize_logger():
    """
    Configura el sistema de logging para registrar eventos y errores.

    Returns:
        logging.Logger: Instancia configurada del logger.
    """
    logger = logging.getLogger("yarvis_logger")
    logger.setLevel(logging.DEBUG)

    # Formato del log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Manejo de archivo de log
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Manejo de salida en consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Añadir manejadores al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instancia global del logger
logger = initialize_logger()

def log_event(level, message):
    """
    Registra un evento o error en el sistema de logs.

    Args:
        level (str): Nivel del log ('info', 'debug', 'warning', 'error', 'critical').
        message (str): Mensaje del evento.
    """
    if level == 'info':
        logger.info(message)
    elif level == 'debug':
        logger.debug(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'critical':
        logger.critical(message)
    else:
        logger.info(f"Nivel no reconocido: {level}. Mensaje: {message}")
