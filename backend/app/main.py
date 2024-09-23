from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)

@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()

app.include_router(router, prefix="/api")