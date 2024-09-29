from app.models.player import Player
from app.models.monster import Monster
from app.services.enemy_service import EnemyService
from app.services.player_service import PlayerService
from app.services.turn_service import TurnService
import random


class CombatService:
    def __init__(
        self,
        player_service: PlayerService,
        enemy_service: EnemyService,
        turn_service: TurnService,
    ):
        self.player_service = player_service
        self.enemy_service = enemy_service
        self.turn_service = turn_service

    async def start_combat(self, player: Player) -> dict:
        if player.current_enemy is not None:
            return {"message": "Combat already started"}

        enemy = self.enemy_service.GenerateEnemy(player.level)
        player.current_enemy = enemy

        response = await self.player_service.update_player(player.id, player)
        if response:
            return {"message": f"Combat started for {player.name}", "enemy": enemy}
        return {"message": "An error occurred while starting the combat"}

    async def combat_status(self, player: Player, combat_actions: dict) -> dict:
        if not player.current_enemy:
            return {"message": "Player not in combat"}

        status = {
            f"{player.name} health": player.current_hp,
            f"{player.current_enemy.name} health": player.current_enemy.current_hp,
        }

        return {"status": status, "actions": combat_actions.get("take a turn", {})}

    async def attack(self, player: Player) -> dict:
        if not player.current_enemy:
            return {"message": "Player not in combat"}

        log = []
        log.append(self.turn_service.take_turn(player, player.current_enemy, 1))
        enemy_action = random.randint(1, 2)
        log.append(
            self.turn_service.take_turn(player.current_enemy, player, enemy_action)
        )

        return {"log": log}

    async def defend(self, player: Player) -> dict:
        if not player.current_enemy:
            return {"message": "Player not in combat"}

        log = []
        log.append(self.turn_service.take_turn(player, player.current_enemy, 2))
        enemy_action = random.randint(1, 2)
        log.append(
            self.turn_service.take_turn(player.current_enemy, player, enemy_action)
        )

        return {"log": log}

    async def get_ability_menu(self, player: Player) -> dict:
        ability_list = player.abilities
        return {
            "message": f"{player.name} abilities",
            "use": "/combat/ability/{ability_id}",
            "abilities": ability_list,
        }

    async def use_ability(self, player: Player, ability_id: int) -> dict:
        # TODO: Implement ability logic
        return {"message": f"{player.name} used ability {ability_id}"}
