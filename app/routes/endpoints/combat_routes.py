import random
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.models.player import Player
from app.services.combat_service import CombatService
from app.services.player_service import PlayerService
from app.services.enemy_service import EnemyService

router = APIRouter(prefix="/combat")


def get_combat_service(
    player_service: PlayerService = Depends(PlayerService.get_player_service),
    enemy_service: EnemyService = Depends(),
):
    return CombatService(player_service, enemy_service)


@router.get("/", response_model=dict)
async def combat_home(request: Request):
    user = getattr(request.state, "user", None)
    if user:
        return {
            "message": "Welcome to the combat home",
            "actions": {
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
            },
        }
    else:
        return RedirectResponse(url="/")


@router.get("/start", response_model=dict)
async def start_combat(
    request: Request,
    combat_service: CombatService = Depends(get_combat_service),
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = Player.model_validate(response["player"])

    if not player:
        return {"message": "Player does not exist"}

    return await combat_service.start_combat(player)


@router.get("/attack", response_model=dict)
async def attack(
    request: Request,
    combat_service: CombatService = Depends(get_combat_service),
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = Player.model_validate(response["player"])
    if not player:
        return {"message": "Player does not exist"}

    return await combat_service.attack(player)


@router.get("/defend", response_model=dict)
async def defend(
    request: Request,
    combat_service: CombatService = Depends(get_combat_service),
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = Player.model_validate(response["player"])

    if not player:
        return {"message": "Player does not exist"}

    return await combat_service.defend(player)


@router.get("/ability", response_model=dict)
async def ability_menu(
    request: Request,
    combat_service: CombatService = Depends(get_combat_service),
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = Player.model_validate(response["player"])
    if not player:
        return {"message": "Player does not exist"}

    return await combat_service.get_ability_menu(player)


@router.get("/ability/{ability_id}", response_model=dict)
async def use_ability(
    request: Request,
    ability_id: int,
    combat_service: CombatService = Depends(get_combat_service),
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = Player.model_validate(response["player"])
    if not player:
        return {"message": "Player does not exist"}

    return await combat_service.use_ability(player, ability_id)
