import random
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.routes.endpoints.player_routes import get_player_service
from app.services.enemy_service import EnemyService
from app.services.player_service import PlayerService

router = APIRouter(prefix="/combat")

def get_enemy_service():
	"""
	Retorna:
		EnemyService: Una instancia del servicio de enemigos con sus dependencias inyectadas.
	"""
	return EnemyService()

@router.get("/", response_model=dict)
async def combat_home(request: Request):
	user = getattr(request.state, 'user', None)
	if user:
		return {
			"message": "Welcome to the combat home",
			"actions": {
				"create a combat": ["/combat/start", "This is for starting a combat"],
				"take a turn": {
					"attack": ["/combat/attack", "This is for attacking the enemy"],
					"defend": ["/combat/defend", "This is for defending from the enemy"],
					"ability": ["/combat/ability", "This is the menu for using abilities"],
					#"heal": "/combat/heal: this is for healing your character"
				},
				"home": ["/", "Return to the home page"]
			}
		}
	else:
		return RedirectResponse(url="/")

@router.get("/start", response_model=dict)
async def start_combat(request: Request, 
					   playerService: PlayerService = Depends(get_player_service),
					   enemyService: EnemyService = Depends(get_enemy_service)):
	user = getattr(request.state, 'user', None)
	if not user:
		return RedirectResponse(url="/")
	
	player = await playerService.get_player_by_name(user)
	if not player:
		return {
			"message": "Player does not exist"
		}
	
	if player["current_enemy"]:
		return {
			"message": "Combat already started"
		}
	
	enemy = await enemyService.get_random_enemy(player["level"])
	player["current_enemy"] = enemy
	
	return {
		"message": f"Combat started for {user}",
		"enemy": enemy
	}

@router.get("/attack", response_model=dict)
async def attack(request: Request, playerService: PlayerService = Depends(get_player_service)):
	user = getattr(request.state, 'user', None)
	if not user:
		return RedirectResponse(url="/")
	
	player = await playerService.get_player_by_name(user)
	if not player:
		return {
			"message": "Player does not exist"
		}
	
	log = []

	log.append(player.TakeTurn(player["current_enemy"], 1))
	enemyAction = random.randint(1, 2)
	log.append(player["current_enemy"].TakeTurn(player, enemyAction))
	
	return {
		"log": log
	}

@router.get("/defend", response_model=dict)
async def defend(request: Request, playerService: PlayerService = Depends(get_player_service)):
	user = getattr(request.state, 'user', None)
	if not user:
		return RedirectResponse(url="/")
	
	player = await playerService.get_player_by_name(user)
	if not player:
		return {
			"message": "Player does not exist"
		}
	
	log = []

	log.append(player.TakeTurn(player["current_enemy"], 2))
	enemyAction = random.randint(1, 2)
	log.append(player["current_enemy"].TakeTurn(player, enemyAction))
	return {
		"message": f"{user} defended"
	}

@router.get("/ability", response_model=dict)
async def ability_menu(request: Request, playerService: PlayerService = Depends(get_player_service)):
	user = getattr(request.state, 'user', None)
	if not user:
		return RedirectResponse(url="/")
	
	player = await playerService.get_player_by_name(user)
	if not player:
		return {
			"message": "Player does not exist"
		}
	
	abilityList = player["abilities"]
	return {
		"message": f"{user} abilities",
		"use": "/combat/ability/{ability_id}",
		"abilities": abilityList
	}

@router.get("/ability/{ability_id}", response_model=dict)
async def use_ability(request: Request, ability_id: int, playerService: PlayerService = Depends(get_player_service)):
	user = getattr(request.state, 'user', None)
	if not user:
		return RedirectResponse(url="/")
	
	player = await playerService.get_player_by_name(user)
	if not player:
		return {
			"message": "Player does not exist"
	}

	#TODO: Implement ability logic
	return {
		"message": f"{user} used ability {ability_id}"
	}