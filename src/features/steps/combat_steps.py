
from behave import given, when, then
from unittest.mock import AsyncMock
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database.mongo.queries.player import PlayerQueries
from app.models.player import Player
from app.services.combat_service import CombatService
from app.services.enemy_service import EnemyService
from app.services.player_service import PlayerService

def mock_db():
    mock_db = AsyncMock(spec=AsyncIOMotorDatabase)
    mock_collection = AsyncMock()
    mock_db.players = mock_collection
    return mock_db


def player_queries(mock_db):
    return PlayerQueries(mock_db)


def player_service(player_queries):
    return PlayerService(player_queries)

def initial_context(context):
    context.mock_db = mock_db()
    context.player_queries = player_queries(context.mock_db)
    context.player_service = player_service(context.player_queries)
    context.enemy_service = EnemyService()
    context.combat_service = CombatService(context.player_service, context.enemy_service)
    context.player = Player(name="Steve")


@given('a player not in combat')
def step_impl_start_combat(context):
    initial_context(context)

@when('the player start the combat')
def step_impl_start_combat(context):
    context.player.current_enemy = context.enemy_service.GenerateEnemy(context.player.level)

@then('the player is in combat')
def step_impl_start_combat(context):
    assert context.player.current_enemy is not None

@given('a player in combat and the enemy with {hp} HP')
def step_impl_attack_enemy(context, hp):
    initial_context(context)
    context.player.current_enemy = context.enemy_service.GenerateEnemy(context.player.level)
    context.player.current_enemy.current_hp = hp
    context.player.current_enemy.name = "Goblin"
    print(context.player.current_enemy.__dict__)

@when('the player attacks')
def step_impl_attack_enemy(context):
    context.combat_service.attack(context.player.__dict__)

@then('the enemy should have less than {hp} HP')
def step_impl_attack_enemy(context, hp):
    print(context.player.current_enemy.__dict__)
    assert int(context.player.current_enemy.current_hp) < int(hp)

