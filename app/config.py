from pydantic_settings import BaseSettings

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
    SALT_ROUNDS: int = 10
    JWT_SECRET_KEY: str = "secret-4235324-56-346-456-43-56-34-57"
# Instancia de la clase Settings para acceder a la configuración
settings = Settings()