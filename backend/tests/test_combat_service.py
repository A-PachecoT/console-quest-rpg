import pytest
from app.services.combat_service import CombatService
from app.models.character import Character
from app.models.monster import Monster

@pytest.fixture
def character():
    return Character(
        id=1,
        name="Test Hero",
        level=1,
        max_hp=100,
        current_hp=100,
        attack=10,
        defense=5,
        xp=0,
        gold=0,
        inventory=[],
        skills=["fireball", "ice_shard"]
    )

@pytest.fixture
def monster():
    return Monster(
        id=1,
        name="Test Monster",
        max_hp=50,
        current_hp=50,
        attack=8,
        defense=3,
        xp_reward=10,
        gold_reward=5
    )

def test_initiate_combat():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, current_hp=100, attack=10, defense=5)
    monster = Monster(id=1, name="Goblin", hp=30, current_hp=30, attack=5, defense=2, xp_reward=10, gold_reward=5)
    
    combat_log = combat_service.initiate_combat(character, [monster])
    
    assert isinstance(combat_log, list)
    assert len(combat_log) > 0
    assert "¡Combate iniciado!" in combat_log[0]

def test_character_turn():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, current_hp=100, attack=10, defense=5)
    monster = Monster(id=1, name="Goblin", hp=30, current_hp=30, attack=5, defense=2, xp_reward=10, gold_reward=5)
    
    log = combat_service._character_turn(character, [monster])
    
    assert isinstance(log, list)
    assert len(log) > 0
    assert "Hero" in log[0] and "Goblin" in log[0]

def test_monster_turn():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, current_hp=100, attack=10, defense=5)
    monster = Monster(id=1, name="Goblin", hp=30, current_hp=30, attack=5, defense=2, xp_reward=10, gold_reward=5)
    
    log = combat_service._monster_turn(monster, character)
    
    assert isinstance(log, list)
    assert len(log) > 0
    assert "Goblin" in log[0] and "Hero" in log[0]

def test_calculate_damage():
    combat_service = CombatService()
    damage = combat_service._calculate_damage(10, 5)
    
    assert isinstance(damage, int)
    assert damage > 0

def test_select_action():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, attack=10, defense=5, skills=["fireball"])
    
    action = combat_service._select_action(character)
    
    assert action in ["basic_attack", "fireball"]

def test_use_skill():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, attack=10, defense=5)
    
    damage, effect = combat_service._use_skill(character, "fireball")
    
    assert isinstance(damage, (int, float))
    assert damage > character.attack
    assert isinstance(effect, str)

def test_calculate_rewards():
    combat_service = CombatService()
    character = Character(id=1, name="Hero", max_hp=100, current_hp=100, attack=10, defense=5, xp=0, gold=0)
    monsters = [
        Monster(id=1, name="Goblin", max_hp=30, current_hp=0, attack=5, defense=2, xp_reward=10, gold_reward=5),
        Monster(id=2, name="Orc", max_hp=50, current_hp=0, attack=8, defense=3, xp_reward=20, gold_reward=10)
    ]
    
    xp_gained, gold_gained = combat_service.calculate_rewards(character, monsters)
    
    assert xp_gained == 30
    assert gold_gained == 15
    assert character.xp == 30
    assert character.gold == 15
