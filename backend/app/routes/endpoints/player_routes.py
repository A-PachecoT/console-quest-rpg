from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.player import Player
from app.services.player_service import PlayerService
from app.database.mongo.queries import PlayerQueries
from app.database.mongo.connection import get_database

router = APIRouter()

def get_player_service():
    """
    Retorna:
        PlayerService: Una instancia del servicio de jugadores con sus dependencias inyectadas.
    """
    db = get_database()
    player_queries = PlayerQueries(db)
    return PlayerService(player_queries)

@router.post("/players", response_model=str)
async def create_player(player: Player, service: PlayerService = Depends(get_player_service)):
    """
    Crea un nuevo jugador.
    Args:
        player (Player): Los datos del jugador a crear.
        service (PlayerService): El servicio de jugadores.
    Retorna:
        str: El ID del jugador creado.
    """
    player_id = await service.create_player(player)
    return player_id

@router.get("/players/{player_id}", response_model=Player)
async def get_player(player_id: str, service: PlayerService = Depends(get_player_service)):
    """
    Obtiene un jugador por su ID.
    Args:
        player_id (str): El ID del jugador a obtener.
        service (PlayerService): El servicio de jugadores.
    Retorna:
        Player: Los datos del jugador.
    Lanza:
        HTTPException: Si el jugador no se encuentra.
    """
    player = await service.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return player

@router.get("/players", response_model=List[Player])
async def get_all_players(service: PlayerService = Depends(get_player_service)):
    """
    Obtiene todos los jugadores.
    Args:
        service (PlayerService): El servicio de jugadores.
    Retorna:
        List[Player]: Una lista con todos los jugadores.
    """
    return await service.get_all_players()

@router.put("/players/{player_id}", response_model=bool)
async def update_player(player_id: str, player: Player, service: PlayerService = Depends(get_player_service)):
    """
    Actualiza los datos de un jugador.
    Args:
        player_id (str): El ID del jugador a actualizar.
        player (Player): Los nuevos datos del jugador.
        service (PlayerService): El servicio de jugadores.
    Retorna:
        bool: True si la actualización fue exitosa.
    Lanza:
        HTTPException: Si el jugador no se encuentra.
    """
    updated = await service.update_player(player_id, player)
    if not updated:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return True

@router.delete("/players/{player_id}", response_model=bool)
async def delete_player(player_id: str, service: PlayerService = Depends(get_player_service)):
    """
    Elimina un jugador.
    Args:
        player_id (str): El ID del jugador a eliminar.
        service (PlayerService): El servicio de jugadores.
    Retorna:
        bool: True si la eliminación fue exitosa.
    Lanza:
        HTTPException: Si el jugador no se encuentra.
    """
    deleted = await service.delete_player(player_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return True
