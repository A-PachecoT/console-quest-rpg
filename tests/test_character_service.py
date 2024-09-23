import pytest
from app.services.character_service import CharacterService
from app.models.entity import Character

@pytest.fixture
def character_service():
    return CharacterService()

def test_create_character(character_service):
    character = Character(id=0, name="Test Character", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    created_character = character_service.create_character(character)
    assert created_character.id == 1
    assert created_character.name == "Test Character"

def test_get_character(character_service):
    character = Character(id=0, name="Test Character", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    created_character = character_service.create_character(character)
    retrieved_character = character_service.get_character(created_character.id)
    assert retrieved_character is not None
    assert retrieved_character.name == "Test Character"

def test_update_character(character_service):
    character = Character(id=0, name="Test Character", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    created_character = character_service.create_character(character)
    updated_character = Character(id=created_character.id, name="Updated Character", level=2, current_hp=120, max_hp=120, attack=12, defense=6)
    result = character_service.update_character(created_character.id, updated_character)
    assert result is not None
    assert result.name == "Updated Character"
    assert result.level == 2

def test_delete_character(character_service):
    character = Character(id=0, name="Test Character", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    created_character = character_service.create_character(character)
    result = character_service.delete_character(created_character.id)
    assert result is True
    assert character_service.get_character(created_character.id) is None

def test_level_up(character_service):
    character = Character(id=0, name="Test Character", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    created_character = character_service.create_character(character)
    leveled_up_character = character_service.level_up(created_character.id)
    assert leveled_up_character is not None
    assert leveled_up_character.level == 2
    assert leveled_up_character.current_hp == 110
    assert leveled_up_character.max_hp == 110
    assert leveled_up_character.attack == 12
    assert leveled_up_character.defense == 6