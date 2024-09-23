from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database

class MongoConnection:
    client: AsyncIOMotorClient = None
    db: Database = None

    @classmethod
    def connect_to_mongo(cls, mongo_url: str, db_name: str):
        cls.client = AsyncIOMotorClient(mongo_url)
        cls.db = cls.client[db_name]

    @classmethod
    def get_db(cls) -> Database:
        return cls.db

    @classmethod
    def close_mongo_connection(cls):
        cls.client.close()

def get_database() -> Database:
    return MongoConnection.get_db()
