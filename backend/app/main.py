from fastapi import FastAPI, HTTPException
from .models.character import Character
from .models.monster import Monster
from .services.character_service import CharacterService
from .services.dungeon_service import DungeonService

app = FastAPI()

character_service = CharacterService()
dungeon_service = DungeonService()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)