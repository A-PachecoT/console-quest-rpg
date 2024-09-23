from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.player import Player
from app.services.player_service import PlayerService
from app.database.mongo.queries import PlayerQueries
from app.database.mongo.connection import get_database

router = APIRouter()

def get_player_service():
    db = get_database()
    player_queries = PlayerQueries(db)
    return PlayerService(player_queries)

@router.post("/players", response_model=str)
async def create_player(player: Player, service: PlayerService = Depends(get_player_service)):
    player_id = await service.create_player(player)
    return player_id

@router.get("/players/{player_id}", response_model=Player)
async def get_player(player_id: str, service: PlayerService = Depends(get_player_service)):
    player = await service.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/players", response_model=List[Player])
async def get_all_players(service: PlayerService = Depends(get_player_service)):
    return await service.get_all_players()

@router.put("/players/{player_id}", response_model=bool)
async def update_player(player_id: str, player: Player, service: PlayerService = Depends(get_player_service)):
    updated = await service.update_player(player_id, player)
    if not updated:
        raise HTTPException(status_code=404, detail="Player not found")
    return True

@router.delete("/players/{player_id}", response_model=bool)
async def delete_player(player_id: str, service: PlayerService = Depends(get_player_service)):
    deleted = await service.delete_player(player_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Player not found")
    return True
