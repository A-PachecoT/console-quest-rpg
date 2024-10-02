from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import jwt
from app.utils.logger import main_logger, api_logger
from prometheus_client import Counter, Histogram
import time

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Console Quest API",
    description="This is the API for the Console Quest project",
    version="1.0.0",
)

REQUESTS = Counter("http_requests_total", "Total HTTP Requests", ["method", "endpoint"])
LATENCY = Histogram(
    "http_request_duration_seconds", "HTTP request latency", ["method", "endpoint"]
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


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    REQUESTS.labels(method=request.method, endpoint=request.url.path).inc()
    LATENCY.labels(method=request.method, endpoint=request.url.path).observe(
        process_time
    )
    api_logger.info(
        f'"{request.method} {request.url.path} HTTP/1.1" {response.status_code}'
    )
    return response


# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/views"), name="static")


@app.on_event("startup")
async def startup_db_client():
    main_logger.info("Starting up database client")
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)
    main_logger.info("Database client started successfully")


@app.on_event("shutdown")
async def shutdown_db_client():
    main_logger.info("Shutting down database client")
    MongoConnection.close_mongo_connection()
    main_logger.info("Database client shut down successfully")


# Incluimos el router de la aplicación con el prefijo "/api"
app.include_router(router)

# Configuramos Prometheus para instrumentar y exponer métricas de la aplicación
Instrumentator().instrument(app).expose(app)

main_logger.info("Application started")
