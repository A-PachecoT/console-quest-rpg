from .endpoints.general_routes import router as general_routes
from .endpoints.player_routes import router as player_routes
from .endpoints.combat_routes import router as combat_routes

from fastapi import APIRouter

router = APIRouter()

router.include_router(general_routes)
router.include_router(player_routes)
router.include_router(combat_routes)
