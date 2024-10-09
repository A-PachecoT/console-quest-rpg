from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import jwt
from rich.console import Console
from rich.markdown import Markdown
import logging

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Console Quest API",
    description="This is the API for the Console Quest project",
    version="1.0.0",
)

# Set up logging
main_logger = logging.getLogger("main")
db_logger = logging.getLogger("database")


def generate_markdown_banner():
    markdown = Markdown(
        """
# 🎮 Console Quest RPG ⚔️
### Made with ❤️ in Perú
### By Pacheco André, Pezo Sergio, Torres Oscar 2️⃣ 0️⃣ 2️⃣ 4️⃣
- **Powered by**: FastAPI
- **Status**: Initializing...
---
Console Quest RPG is a turn-based role-playing game developed as a software project for the CC3S2 course at the National University of Engineering. The game uses FastAPI for the backend and is designed to be played through API calls.
---

"""
    )
    return markdown


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

    # Initialize the instrumentator
    instrumentator.expose(app)


@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()
