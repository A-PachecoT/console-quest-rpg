from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Console Quest API",
    description="This is the API for the Console Quest project",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_db_client():
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)

@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()


# Incluimos el router de la aplicación con el prefijo "/api"
app.include_router(router, prefix="/api")

# Configuramos Prometheus para instrumentar y exponer métricas de la aplicación
Instrumentator().instrument(app).expose(app)