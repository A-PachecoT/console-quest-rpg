from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
    assert response.status_code == 200
    assert response.json() == {"message": f"{welcome_message}"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_game_info():
    response = client.get("/game-info")
    assert response.status_code == 200
    assert response.json() == {
        "name": "RPG Game",
        "version": "0.3.0",
        "description": "A turn-based RPG game with FastAPI backend"
    }

def test_create_character():
    character_data = {
        "id": 0,
        "name": "Test Hero",
        "level": 1,
        "hp": 100,
        "max_hp": 100,
        "attack": 10,
        "defense": 5,
        "experience": 0,
        "inventory": []
    }
    response = client.post("/characters", json=character_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Hero"
    assert response.json()["id"] == 1

def test_get_character():
    response = client.get("/characters/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Hero"

def test_update_character():
    update_data = {
        "id": 1,
        "name": "Updated Hero",
        "level": 2,
        "hp": 120,
        "max_hp": 120,
        "attack": 12,
        "defense": 6,
        "experience": 100,
        "inventory": ["Potion"]
    }
    response = client.put("/characters/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Hero"
    assert response.json()["level"] == 2

def test_delete_character():
    response = client.delete("/characters/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Character deleted successfully"}

def test_level_up_character():
    # First, create a new character
    character_data = {
        "id": 0,
        "name": "Leveling Hero",
        "level": 1,
        "hp": 100,
        "max_hp": 100,
        "attack": 10,
        "defense": 5,
        "experience": 0,
        "inventory": []
    }
    create_response = client.post("/characters", json=character_data)
    character_id = create_response.json()["id"]

    # Now, level up the character
    response = client.post(f"/characters/{character_id}/level-up")
    assert response.status_code == 200
    assert response.json()["level"] == 2
    assert response.json()["max_hp"] == 110
    assert response.json()["attack"] == 12
    assert response.json()["defense"] == 6

def test_generate_dungeon():
    response = client.post("/dungeon/generate")
    assert response.status_code == 200
    assert "dungeon" in response.json()
    assert len(response.json()["dungeon"]) > 0

def test_move_player():
    # First, generate a dungeon
    client.post("/dungeon/generate")

    # Now, try to move the player
    response = client.post("/dungeon/move/right")
    assert response.status_code == 200
    assert "message" in response.json()

def test_move_player_invalid_direction():
    response = client.post("/dungeon/move/invalid")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid direction"