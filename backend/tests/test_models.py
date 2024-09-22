import pytest
from app.models.character import Character
from app.models.monster import Monster
from app.models.item import Item, ItemType

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
    assert character.inventory == []

def test_monster_creation():
    monster = Monster(id=1, name="Goblin", current_hp=50, max_hp=50, attack=5, defense=2, xp_reward=10)
    assert monster.id == 1
    assert monster.name == "Goblin"
    assert monster.current_hp == 50
    assert monster.max_hp == 50
    assert monster.attack == 5
    assert monster.defense == 2
    assert monster.xp_reward == 10

def test_item_creation():
    item = Item(id=1, name="Sword", type=ItemType.WEAPON, value=15, description="A sharp sword")
    assert item.id == 1
    assert item.name == "Sword"
    assert item.type == ItemType.WEAPON
    assert item.value == 15
    assert item.description == "A sharp sword"

def test_item_type_enum():
    assert ItemType.WEAPON == "weapon"
    assert ItemType.ARMOR == "armor"
    assert ItemType.POTION == "potion"