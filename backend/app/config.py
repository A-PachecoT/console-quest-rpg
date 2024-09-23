from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """
    Clase de configuración que utiliza pydantic_settings.

    Esta configuración está diseñada para funcionar con Docker.

    Atributos:
        MONGO_URL (str): La URL de conexión a la base de datos MongoDB.
            En un entorno Docker, esto generalmente apunta al servicio de MongoDB definido en docker-compose.
        MONGO_DB_NAME (str): El nombre de la base de datos MongoDB a utilizar.
    """
    MONGO_URL: str
    MONGO_DB_NAME: str

    class Config:
        env_file = ".env"

# Instancia de la clase Settings para acceder a la configuración
settings = Settings()