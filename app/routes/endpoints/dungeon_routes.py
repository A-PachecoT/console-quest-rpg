from fastapi import APIRouter, HTTPException
from app.services.dungeon_service import DungeonService

router = APIRouter()
dungeon_service = DungeonService()

@router.post("/dungeon/generate")
async def generate_dungeon():
    dungeon = dungeon_service.generate_dungeon()
    return {"dungeon": dungeon}

@router.post("/dungeon/move/{direction}")
async def move_player(direction: str):
    if direction not in ["up", "down", "left", "right"]:
        raise HTTPException(status_code=400, detail="Invalid direction")
    if dungeon_service.move_player(direction):
        return {"message": f"Player moved {direction} successfully"}
    else:
        return {"message": "Player couldn't move in that direction"}