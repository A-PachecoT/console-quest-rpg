import pytest
from ..app.models.character import Character
from ..app.models.monster import Monster
from ..app.services.combat_service import CombatService

@pytest.fixture
def character():
    return Character(
        id=1,
        name="Hero",
        level=1,
        max_hp=100,
        current_hp=100,
        attack=10,
        defense=5,
        xp=0,
        gold=0,
        inventory=["Potion", "Sword"],
        skills=["fireball", "ice_shard"]
    )

@pytest.fixture
def monsters():
    return [
        Monster(
            id=1,
            name="Goblin",
            current_hp=50,
            max_hp=50,
            attack=5,
            defense=2,
            xp_reward=10,
            gold_reward=5
        ),
        Monster(
            id=2,
            name="Orc",
            current_hp=80,
            max_hp=80,
            attack=8,
            defense=3,
            xp_reward=20,
            gold_reward=10
        )
    ]

def test_combat(character, monsters):
    combat_id = "test_combat_1"
    CombatService.initiate_combat(combat_id, character, monsters)

    # Character's turn: basic attack on Goblin
    log = CombatService.character_turn(combat_id, "basic_attack", 0)
    assert "Hero realiza un ataque básico a Goblin causando" in log[-1]

    # Monster's turn
    log = CombatService.monster_turn(combat_id)
    assert "Goblin ataca a Hero causando" in log[-1] or "Orc ataca a Hero causando" in log[-1]

    # Character's turn: use skill on Orc
    log = CombatService.character_turn(combat_id, "fireball", 1)
    assert "Hero usa fireball contra Orc causando" in log[-1]

    # Monster's turn
    log = CombatService.monster_turn(combat_id)
    assert "Goblin ataca a Hero causando" in log[-1] or "Orc ataca a Hero causando" in log[-1]

    # Continue combat until one side wins
    while character.current_hp > 0 and any(monster.current_hp > 0 for monster in monsters):
        log = CombatService.character_turn(combat_id, "basic_attack", 0)
        log = CombatService.monster_turn(combat_id)

    # Check combat result
    if character.current_hp <= 0:
        assert "Hero ha sido derrotado." in log[-1]
    else:
        assert "¡Todos los monstruos han sido derrotados!" in log[-1]

    # Check combat log
    combat_log = CombatService.get_combat_log(combat_id)
    assert len(combat_log) > 0
