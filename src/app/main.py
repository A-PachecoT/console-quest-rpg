from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator, metrics
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


# Incluimos el router de la aplicación con el prefijo "/api"
app.include_router(router)

# Configure Prometheus to instrument and expose metrics for the application
instrumentator = Instrumentator().instrument(app)
instrumentator.add(
    metrics.requests(
        metric_name="http_all_requests",
    )
)
instrumentator.add(
    metrics.latency(
        metric_name="http_all_request_duration_seconds",
    )
)

# Initialize the instrumentator


@app.on_event("startup")
async def startup_db_client():
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)
    instrumentator.expose(app)


@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()
