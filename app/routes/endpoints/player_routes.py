from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.player import Player
from app.services.player_service import PlayerService
from app.database.mongo.queries import PlayerQueries
from app.database.mongo.connection import get_database

router = APIRouter(prefix="/player")

def get_player_service():
    """
    Retorna:
        PlayerService: Una instancia del servicio de jugadores con sus dependencias inyectadas.
    """
    db = get_database()
    player_queries = PlayerQueries(db)
    return PlayerService(player_queries)

@router.get("/", response_model=dict)
async def player_home():
    return {
        "message": "Welcome to the player home",
        "actions": {
            "create_player": "/player/create/{name}",
            "get_all_players": "/player/all",
            "get_player_by_name": "/player/getByName/{name}"
        }
    }

@router.get("/create/{name}", response_model=dict)
async def create_player(name: str, service: PlayerService = Depends(get_player_service)):
    
    player_id = await service.create_player(name)
    return player_id

@router.get("/all", response_model=dict)
async def get_all_players(service: PlayerService = Depends(get_player_service)):
    players = await service.get_all_players()
    if len(players) == 0:
        raise HTTPException(status_code=404, detail="No players found")
    return players

@router.get("/getByName/{name}", response_model=dict)
async def get_player_by_name(name: str, service: PlayerService = Depends(get_player_service)):
    player = await service.get_player_get_by_name(name)
    return player
#@router.put("/players/{player_id}", response_model=bool)
#async def update_player(player_id: str, player: Player, service: PlayerService = Depends(get_player_service)):
#    """
#    Actualiza los datos de un jugador.
#    Args:
#        player_id (str): El ID del jugador a actualizar.
#        player (Player): Los nuevos datos del jugador.
#        service (PlayerService): El servicio de jugadores.
#    Retorna:
#        bool: True si la actualización fue exitosa.
#    Lanza:
#        HTTPException: Si el jugador no se encuentra.
#    """
#    updated = await service.update_player(player_id, player)
#    if not updated:
#        raise HTTPException(status_code=404, detail="Jugador no encontrado")
#    return True

#@router.delete("/players/{player_id}", response_model=bool)
#async def delete_player(player_id: str, service: PlayerService = Depends(get_player_service)):
#    """
#    Elimina un jugador.
#    Args:
#        player_id (str): El ID del jugador a eliminar.
#        service (PlayerService): El servicio de jugadores.
#    Retorna:
#        bool: True si la eliminación fue exitosa.
#    Lanza:
#        HTTPException: Si el jugador no se encuentra.
#    """
#    deleted = await service.delete_player(player_id)
#    if not deleted:
#        raise HTTPException(status_code=404, detail="Jugador no encontrado")
#    return True

def error_ocurred(name_error:str):
    return "An error ocurred in player " + name_error