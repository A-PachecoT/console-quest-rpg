from fastapi import FastAPI, HTTPException
from .models.character import Character
from .models.monster import Monster
from .services.character_service import CharacterService
from .services.dungeon_service import DungeonService
from .services.combat_service import CombatService
from typing import List

app = FastAPI()

character_service = CharacterService()
dungeon_service = DungeonService()
combat_service = CombatService()

@app.get("/")
async def root():
    welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
    return {"message": f"{welcome_message}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/game-info")
async def game_info():
    return {
        "name": "RPG Game",
        "version": "0.3.0",
        "description": "A turn-based RPG game with FastAPI backend"
    }

@app.post("/characters", response_model=Character)
async def create_character(character: Character):
    return character_service.create_character(character)

@app.get("/characters/{character_id}", response_model=Character)
async def get_character(character_id: int):
    character = character_service.get_character(character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.put("/characters/{character_id}", response_model=Character)
async def update_character(character_id: int, character: Character):
    updated_character = character_service.update_character(character_id, character)
    if updated_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return updated_character

@app.delete("/characters/{character_id}")
async def delete_character(character_id: int):
    if not character_service.delete_character(character_id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character deleted successfully"}

@app.post("/characters/{character_id}/level-up", response_model=Character)
async def level_up_character(character_id: int):
    leveled_up_character = character_service.level_up(character_id)
    if leveled_up_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return leveled_up_character

@app.post("/dungeon/generate")
async def generate_dungeon():
    dungeon = dungeon_service.generate_dungeon()
    return {"dungeon": dungeon}

@app.post("/dungeon/move/{direction}")
async def move_player(direction: str):
    if direction not in ["up", "down", "left", "right"]:
        raise HTTPException(status_code=400, detail="Invalid direction")
    if dungeon_service.move_player(direction):
        return {"message": f"Player moved {direction} successfully"}
    else:
        return {"message": "Player couldn't move in that direction"}

@app.post("/combat/initiate")
async def initiate_combat(character_id: int, monster_ids: List[int]):
    character = character_service.get_character(character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    monsters = [dungeon_service.get_monster(monster_id) for monster_id in monster_ids]
    if not all(monsters):
        raise HTTPException(status_code=404, detail="One or more monsters not found")
    
    combat_log = combat_service.initiate_combat(character, monsters)
    return {"combat_log": combat_log}

@app.post("/combat/attack")
async def perform_attack(character_id: int, monster_id: int):
    character = character_service.get_character(character_id)
    monster = dungeon_service.get_monster(monster_id)
    
    if not character or not monster:
        raise HTTPException(status_code=404, detail="Character or monster not found")
    
    attack_log = combat_service._character_turn(character, [monster])
    return {"attack_log": attack_log}

@app.post("/combat/use-skill")
async def use_skill(character_id: int, monster_id: int, skill_name: str):
    character = character_service.get_character(character_id)
    monster = dungeon_service.get_monster(monster_id)
    
    if not character or not monster:
        raise HTTPException(status_code=404, detail="Character or monster not found")
    
    if skill_name not in character.skills:
        raise HTTPException(status_code=400, detail="Skill not available for this character")
    
    skill_damage, skill_effect = combat_service._use_skill(character, skill_name)
    damage = combat_service._calculate_damage(skill_damage, monster.defense)
    monster.current_hp = max(0, monster.current_hp - damage)
    
    log = [f"{character.name} usa {skill_name} contra {monster.name} causando {damage} de daño."]
    if skill_effect:
        log.append(f"Efecto adicional: {skill_effect}")
    
    return {"skill_log": log}

@app.post("/combat/end")
async def end_combat(character_id: int, defeated_monster_ids: List[int]):
    character = character_service.get_character(character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    defeated_monsters = [dungeon_service.get_monster(monster_id) for monster_id in defeated_monster_ids]
    if not all(defeated_monsters):
        raise HTTPException(status_code=404, detail="One or more monsters not found")
    
    xp_gained, gold_gained = combat_service.calculate_rewards(character, defeated_monsters)
    return {"xp_gained": xp_gained, "gold_gained": gold_gained}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)