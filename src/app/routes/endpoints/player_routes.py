from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.player import Player
from app.services.player_service import PlayerService
from app.database.mongo.queries import PlayerQueries
from app.database.mongo.connection import get_database

router = APIRouter(prefix="/player")


@router.get("/", response_model=dict)
async def player_home():
    return {
        "message": "Welcome to the player home",
        "actions": {"register": "/register", "login": "/login"},
    }


# @router.put("/players/{player_id}", response_model=bool)
# async def update_player(player_id: str, player: Player, service: PlayerService = Depends(get_player_service)):
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

# @router.delete("/players/{player_id}", response_model=bool)
# async def delete_player(player_id: str, service: PlayerService = Depends(get_player_service)):
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


@router.get("/all")
async def get_all_players(
    service: PlayerService = Depends(PlayerService.get_player_service),
):
    return await service.get_all_players()


@router.delete("/delete/all")
async def delete_all_players(
    service: PlayerService = Depends(PlayerService.get_player_service),
):
    return await service.delete_all_players()


def error_ocurred(name_error: str):
    return "An error ocurred in player " + name_error
