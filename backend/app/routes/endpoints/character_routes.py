from fastapi import APIRouter, HTTPException
from app.models.character import Character
from app.services.character_service import CharacterService

router = APIRouter()
character_service = CharacterService()

@router.post("/characters", response_model=Character)
async def create_character(character: Character):
    return character_service.create_character(character)

@router.get("/characters/{character_id}", response_model=Character)
async def get_character(character_id: int):
    character = character_service.get_character(character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.put("/characters/{character_id}", response_model=Character)
async def update_character(character_id: int, character: Character):
    updated_character = character_service.update_character(character_id, character)
    if updated_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return updated_character

@router.delete("/characters/{character_id}")
async def delete_character(character_id: int):
    if not character_service.delete_character(character_id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character deleted successfully"}

@router.post("/characters/{character_id}/level-up", response_model=Character)
async def level_up_character(character_id: int):
    leveled_up_character = character_service.level_up(character_id)
    if leveled_up_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return leveled_up_character