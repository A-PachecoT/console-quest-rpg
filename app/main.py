from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import jwt
from app.utils.logger import (
    main_logger,
    api_logger,
    db_logger,
    player_logger,
    monster_logger,
    combat_logger,
    metrics_logger,
)
from prometheus_client import Counter, Histogram
import time
from rich.console import Console
from rich.markdown import Markdown
from app.metrics import (
    player_damage_metric,
    player_level_metric,
    combat_outcomes_metric,
)


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


def generate_markdown_banner():
    markdown = Markdown(
        """
# 🎮 Console Quest RPG ⚔️
### Made with ❤️ in Perú
<<<<<<< HEAD
### By Pacheco André, Pezo Sergio, Torres Oscar 2️⃣ 0️⃣ 2️⃣ 4️⃣
=======
### By Pacheco André, Pezo Sergio, Torres Oscar 2️⃣0️⃣2️⃣4️⃣
>>>>>>> e94a0d6 (feat(startup): add emojis to markdown banner)
- **Powered by**: FastAPI
- **Status**: Initializing...
---
Console Quest RPG is a turn-based role-playing game developed as a software project for the CC3S2 course at the National University of Engineering. The game uses FastAPI for the backend and is designed to be played through API calls.
---

"""
    )
    return markdown


@app.on_event("startup")
async def startup_event():
    console = Console()
    console.print(generate_markdown_banner())
    main_logger.info("🚀 Starting Console Quest RPG")
    main_logger.info("Initializing services...")
    main_logger.info("Starting up database client")
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)
    db_logger.info(f"Connected to MongoDB at {settings.MONGO_URL}")
    main_logger.info("Database client started successfully")
    main_logger.info("All services initialized")
    main_logger.info("Console Quest RPG is ready to play!")


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
    metrics_logger.info(
        f'"{request.method} {request.url.path} HTTP/1.1" {response.status_code} - {process_time:.4f}s'
    )
    return response


# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/views"), name="static")


@app.on_event("startup")
async def startup_db_client():
    main_logger.info("Starting up database client")
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)
    db_logger.info(f"Connected to MongoDB at {settings.MONGO_URL}")
    main_logger.info("Database client started successfully")


@app.on_event("shutdown")
async def shutdown_db_client():
    main_logger.info("Shutting down database client")
    MongoConnection.close_mongo_connection()
    db_logger.info("Disconnected from MongoDB")
    main_logger.info("Database client shut down successfully")


# Incluimos el router de la aplicación con el prefijo "/api"
app.include_router(router)

main_logger.info("Application started")

# Configure Prometheus to instrument and expose metrics for the application
instrumentator = Instrumentator().instrument(app)
instrumentator.add(
    metrics.requests(
        metric_name="http_all_requests",
    )
)

# Add custom metrics to instrumentator
instrumentator.add(player_damage_metric())
instrumentator.add(player_level_metric())
instrumentator.add(combat_outcomes_metric())


# Initialize the instrumentator
instrumentator.expose(app)
