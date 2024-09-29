from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import jwt

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Console Quest API",
    description="This is the API for the Console Quest project",
    version="1.0.0",
)


@app.middleware("http")
async def token_middleware(request: Request, call_next):
    token = request.cookies.get("access_token")
    if token:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload.get("name")
        except jwt.ExpiredSignatureError:
            request.state.user = None
    return await call_next(request)


# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/views"), name="static")


@app.on_event("startup")
async def startup_db_client():
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)


@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()


# Incluimos el router de la aplicación con el prefijo "/api"
app.include_router(router)

# Configuramos Prometheus para instrumentar y exponer métricas de la aplicación
Instrumentator().instrument(app).expose(app)
