from app.models.player import Player
from app.models.monster import Monster
from app.services.enemy_service import EnemyService
from app.services.player_service import PlayerService
import random


class CombatService:
    def __init__(self, player_service: PlayerService, enemy_service: EnemyService):
        self.player_service = player_service
        self.enemy_service = enemy_service

    async def start_combat(self, player: dict) -> dict:
        if player["current_enemy"] is not None:
            return {"message": "Combat already started"}

        enemy = self.enemy_service.GenerateEnemy(player["level"])
        enemy_dict = enemy.dict()
        player["current_enemy"] = enemy_dict

        response = await self.player_service.update_player(player)
        if response:
            return {
                "message": f"Combat started for {player['name']}",
                "enemy": enemy_dict,
            }
        return {"message": "An error occurred while starting the combat"}

    async def combat_status(self, player: dict, combat_actions: dict) -> dict:
        if not player["current_enemy"]:
            return {"message": "Player not in combat"}

        status = {
            f"{player['name']} health": player["current_hp"],
            f"{player['current_enemy']['name']} health": player["current_enemy"][
                "current_hp"
            ],
        }

        return {"status": status, "actions": combat_actions.get("take a turn", {})}

    async def attack(self, player: dict) -> dict:
        if not player["current_enemy"]:
            return {"message": "Player not in combat"}

        log = []
        log.append(self._take_turn(player, player["current_enemy"], 1))
        enemy_action = random.randint(1, 2)
        log.append(self._take_turn(player["current_enemy"], player, enemy_action))

        await self.player_service.update_player(player)
        return {"log": log}

    async def defend(self, player: dict) -> dict:
        if not player["current_enemy"]:
            return {"message": "Player not in combat"}

        log = []
        log.append(self._take_turn(player, player["current_enemy"], 2))
        enemy_action = random.randint(1, 2)
        log.append(self._take_turn(player["current_enemy"], player, enemy_action))

        await self.player_service.update_player(player)
        return {"log": log}

    def _take_turn(self, entity, target, action: int):
        if action == 1:
            return self._attack(entity, target)
        if action == 2:
            return self._defend(entity)
        return "Invalid action"

    def _attack(self, attacker, target):
        damage_mitigation = (target["defense"]) / (target["defense"] + 5)
        extra_mitigation = 0.3 if target.get("is_defending", False) else 0
        damage = attacker["attack"] * (1 - damage_mitigation) * (1 - extra_mitigation)
        target["current_hp"] -= damage
        target["is_defending"] = False
        return f"{attacker['name']} attacked {target['name']} for {damage} damage"

    def _defend(self, entity):
        entity["is_defending"] = True
        return f"{entity['name']} is defending"

    async def get_ability_menu(self, player: dict) -> dict:
        ability_list = player["abilities"]
        return {
            "message": f"{player['name']} abilities",
            "use": "/combat/ability/{ability_id}",
            "abilities": ability_list,
        }

    async def use_ability(self, player: dict, ability_id: int) -> dict:
        # TODO: Implement ability logic
        result = {"message": f"{player['name']} used ability {ability_id}"}
        await self.player_service.update_player(player)
        return result
