from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from ..services.combat_service import CombatService
from ..models.character import Character
from ..models.monster import Monster

router = APIRouter()

class CombatRequest(BaseModel):
    combat_id: str
    character: Character
    monsters: List[Monster]

class ActionRequest(BaseModel):
    combat_id: str
    action: str
    target_index: int

@router.post("/combat/start")
async def start_combat(request: CombatRequest):
    combat_id = request.combat_id
    character = request.character
    monsters = request.monsters

    if not character or not monsters:
        raise HTTPException(status_code=400, detail="Character and monsters must be provided")

    CombatService.initiate_combat(combat_id, character, monsters)
    return {"message": "Combat started", "combat_id": combat_id}

@router.post("/combat/character-turn")
async def character_turn(request: ActionRequest):
    combat_id = request.combat_id
    action = request.action
    target_index = request.target_index

    log = CombatService.character_turn(combat_id, action, target_index)
    return {"combat_log": log}

@router.post("/combat/monster-turn")
async def monster_turn(combat_id: str):
    log = CombatService.monster_turn(combat_id)
    return {"combat_log": log}

@router.get("/combat/log/{combat_id}")
async def get_combat_log(combat_id: str):
    log = CombatService.get_combat_log(combat_id)
    return {"combat_log": log}