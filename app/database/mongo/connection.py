from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure
from app.config import settings

MONGO_URL = settings.MONGO_URL
MONGO_DB_NAME = settings.MONGO_DB_NAME


class MongoConnection:
    """
    Clase Singleton para manejar la conexión a MongoDB.
    """

    _instance = None
    client: AsyncIOMotorClient = None
    db: Database = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            if MONGO_URL and MONGO_DB_NAME:
                cls.connect_to_mongo(MONGO_URL, MONGO_DB_NAME)

        return cls._instance

    @classmethod
    def connect_to_mongo(cls, mongo_url: str, db_name: str):
        """
        Establece la conexión con MongoDB.

        Args:
            mongo_url (str): URL de conexión a MongoDB.
            db_name (str): Nombre de la base de datos.

        Raises:
            ConnectionFailure: Si no se puede establecer la conexión.
            ValueError: Si los parámetros no son válidos.
        """
        if not mongo_url or not db_name:
            raise ValueError("Both mongo_url and db_name must be provided")

        if cls.client is None:
            try:
                cls.client = AsyncIOMotorClient(mongo_url)
                # Verificar la conexión
                cls.client.admin.command("ismaster")
                cls.db = cls.client[db_name]
            except ConnectionFailure:
                cls.client = None
                cls.db = None
                raise ConnectionFailure("Failed to connect to MongoDB")

    @classmethod
    def get_db(cls) -> Database:
        """
        Obtiene la instancia de la base de datos.

        Returns:
            Database: Instancia de la base de datos MongoDB.

        Raises:
            RuntimeError: Si la conexión no ha sido establecida.
        """
        if cls.db is None:
            raise RuntimeError(
                "Database connection not established. Call connect_to_mongo first."
            )
        return cls.db

    @classmethod
    def close_mongo_connection(cls):
        """
        Cierra la conexión con MongoDB.
        """
        if cls.client:
            cls.client.close()
        cls.client = None
        cls.db = None

    @classmethod
    def is_connected(cls) -> bool:
        """
        Verifica si la conexión está establecida y activa.

        Returns:
            bool: True si la conexión está activa, False en caso contrario.
        """
        if cls.client is None:
            return False
        try:
            cls.client.admin.command("ismaster")
            return True
        except ConnectionFailure:
            return False


def get_database() -> Database:
    """
    Función auxiliar para obtener la instancia de la base de datos.

    Returns:
        Database: Instancia de la base de datos MongoDB.

    Raises:
        RuntimeError: Si la conexión no ha sido establecida.
    """
    if not MongoConnection.is_connected():
        raise RuntimeError("Database connection is not active. Reconnect to MongoDB.")
    return MongoConnection.get_db()
