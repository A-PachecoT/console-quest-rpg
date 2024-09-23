from .endpoints.character_routes import router as character_routes
from .endpoints.general_routes import router as general_routes
from .endpoints.player_routes import router as player_routes

from fastapi import APIRouter

router = APIRouter()

router.include_router(character_routes)
router.include_router(dungeon_routes)
router.include_router(general_routes)
router.include_router(player_routes)



