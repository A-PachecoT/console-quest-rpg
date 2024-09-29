import random
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.models.player import Player
from app.services.combat_service import CombatService
from app.services.player_service import PlayerService
from app.services.enemy_service import EnemyService

router = APIRouter(prefix="/combat")

COMBAT_ACTIONS = {
    "create a combat": ["/combat/start", "This is for starting a combat"],
    "take a turn": {
        "attack": ["/combat/attack", "This is for attacking the enemy"],
        "defend": [
            "/combat/defend",
            "This is for defending from the enemy",
        ],
        "ability": [
            "/combat/ability",
            "This is the menu for using abilities",
        ],
        # "heal": "/combat/heal: this is for healing your character"
    },
    "home": ["/", "Return to the home page"],
}


def get_combat_service(
    player_service: PlayerService = Depends(PlayerService.get_player_service),
    enemy_service: EnemyService = Depends(),
):
    return CombatService(player_service, enemy_service)


# ... (rest of the file remains the same)
