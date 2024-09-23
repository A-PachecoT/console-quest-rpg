import pytest
from app.models.entity import Character
from app.models.monster import Monster

def test_character_creation():
    character = Character(id=1, name="Hero", level=1, current_hp=100, max_hp=100, attack=10, defense=5)
    assert character.id == 1
    assert character.name == "Hero"
    assert character.level == 1
    assert character.current_hp == 100
    assert character.max_hp == 100
    assert character.attack == 10
    assert character.defense == 5
    assert character.xp == 0

def test_monster_creation():
    monster = Monster(id=1, name="Goblin", current_hp=50, max_hp=50, attack=5, defense=2, xp_reward=10)
    assert monster.id == 1
    assert monster.name == "Goblin"
    assert monster.current_hp == 50
    assert monster.max_hp == 50
    assert monster.attack == 5
    assert monster.defense == 2
    assert monster.xp_reward == 10
