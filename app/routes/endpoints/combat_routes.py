from fastapi import APIRouter, Depends

from app.routes.endpoints.player_routes import get_player_service
from app.services.player_service import PlayerService

router = APIRouter(prefix="/combat")

@router.get("/", response_model=dict)
async def combat_home():
	return {
		"message": "Welcome to the combat home",
		"actions": {
			"create a combat": "/combat/{name}/start: this is for starting a combat",
			"take a turn": {
				"attack": "/combat/{name}/attack: this is for attacking the enemy",
				"defend": "/combat/{name}/defend: this is for defending from the enemy",
				"ability": "/combat/{name}/ability: this is the menu for using abilities",
				#"heal": "/combat/{name}/heal: this is for healing your character"
			},
		}
	}

@router.get("/{name}/start", response_model=dict)
async def start_combat(
	name: str, 
	playerService: PlayerService = Depends(get_player_service)):

	player = playerService.get_player_get_by_name(name)

	if not player:
		return {
			"message": "Player does not exist"
		}
	
	if player["current_enemy"]:
		return {
			"message": "Combat already started"
		}
	
	#TODO: Create enemy for the current player
	return {
		"message": f"Combat started for {name}"
	}

@router.get("/{name}/attack")
async def attack(
	name: str, 
	playerService: PlayerService = Depends(get_player_service)):

	player = playerService.get_player_get_by_name(name)

	if not player:
		return {
			"message": "Player does not exist"
		}
	
	#TODO: Implement attack logic
	return {
		"message": f"{name} attacked"
	}

@router.get("/{name}/defend")
async def defend(
	name: str, 
	playerService: PlayerService = Depends(get_player_service)):

	player = playerService.get_player_get_by_name(name)

	if not player:
		return {
			"message": "Player does not exist"
		}
	
	#TODO: Implement defend logic
	return {
		"message": f"{name} defended"
	}

@router.get("/{name}/ability")
async def ability_menu(
	name: str, 
	playerService: PlayerService = Depends(get_player_service)):

	player = playerService.get_player_get_by_name(name)

	if not player:
		return {
			"message": "Player does not exist"
		}
	
	abilityList = player["abilities"]
	return {
		"message": f"{name} abilities",
		"use": "/combat/{name}/ability/{ability_id}",
		"abilities": abilityList
	}

@router.get("/{name}/ability/{ability_id}")
async def use_ability(
	name: str, 
	ability_id: int,
	playerService: PlayerService = Depends(get_player_service)):

	player = playerService.get_player_get_by_name(name)

	if not player:
		return {
			"message": "Player does not exist"
	}

	#TODO: Implement ability logic
	return {
		"message": f"{name} used ability {ability_id}"
	}