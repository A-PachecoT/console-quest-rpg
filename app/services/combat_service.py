from app.models.entity import Entity
from app.models.player import Player
from app.models.monster import Monster
from app.services.enemy_service import EnemyService
from app.services.player_service import PlayerService
import random
from app.utils.logger import combat_logger
import colorlog


class CombatService:
    def __init__(self, player_service: PlayerService, enemy_service: EnemyService):
        self.player_service = player_service
        self.enemy_service = enemy_service

    async def start_combat(self, player: dict) -> dict:
        combat_logger.info(f"Initiating combat for player: {player['name']}")
        if player["current_enemy"] is not None:
            combat_logger.warning(f"Combat already in progress for {player['name']}")
            return {"message": "Combat already started"}

        enemy = self.enemy_service.GenerateEnemy(player["level"])
        enemy_dict = enemy.dict()
        player["current_enemy"] = enemy_dict

        combat_logger.info(f"Combat started: {player['name']} vs {enemy_dict['name']}")
        return {"message": f"Combat started for {player['name']}", "enemy": enemy_dict}

    async def combat_status(self, player: dict, combat_actions: dict) -> dict:
        status = {
            f"{player['name']} health": player["current_hp"],
            f"{player['name']} mana": player["current_mana"],
            f"{player['current_enemy']['name']} health": player["current_enemy"][
                "current_hp"
            ],
            f"{player['current_enemy']['name']} mana": player["current_enemy"][
                "current_mana"
            ],
        }

        return {"status": status, "actions": combat_actions.get("take a turn", {})}

    async def attack(self, player: dict) -> dict:
        log = []
        combat_logger.info(
            f"{player['name']} attacks {player['current_enemy']['name']}"
        )
        log.append(self._take_turn(player, player["current_enemy"], 1))

        if player["current_enemy"]["current_hp"] <= 0:
            combat_logger.info(
                f"{player['name']} has defeated {player['current_enemy']['name']}!"
            )
            levelFlag = self.player_service.add_experience(
                player, player["current_enemy"]["xp_reward"]
            )

            log.append(f"{player['name']} defeated {player['current_enemy']['name']}")
            log.append(
                f"{player['name']} gained {player['current_enemy']['xp_reward']} experience"
            )
            if levelFlag:
                log.append(f"{player['name']} leveled up to level {player['level']}!")
            log.append("To start a combat, go to /combat/start")

            self.enemy_service.die(player)
            await self.player_service.update_player(player)
            return {"log": log}

        enemy_action = random.randint(1, 2)
        combat_logger.info(f"{player['current_enemy']['name']} takes action")
        log.append(self._take_turn(player["current_enemy"], player, enemy_action))

        if player["current_hp"] <= 0:
            combat_logger.warning(
                f"{player['name']} has been defeated by {player['current_enemy']['name']}!"
            )
            log.append(
                f"{player['name']} was defeated by {player['current_enemy']['name']}"
            )
            log.append("Game over")
            log.append("To start a combat, go to /combat/start")

            self.player_service.die(player)
        await self.player_service.update_player(player)
        return {"log": log}

    async def defend(self, player: dict) -> dict:
        log = []
        log.append(self._take_turn(player, player["current_enemy"], 2))
        enemy_action = random.randint(1, 2)
        log.append(self._take_turn(player["current_enemy"], player, enemy_action))

        if player["current_hp"] <= 0:
            log.append(
                f"{player['name']} was defeated by {player['current_enemy']['name']}"
            )
            log.append("Game over")
            log.append("To start a combat, go to /combat/start")

            self.player_service.die(player)

        await self.player_service.update_player(player)
        return {"log": log}

    async def get_ability_menu(self, player: dict) -> dict:
        ability_list = player["abilities"]
        return {
            "message": f"{player['name']} abilities",
            "use": "/combat/ability/{ability_id}",
            "abilities": ability_list,
        }

    async def use_ability(self, player: dict, ability_id: int) -> dict:
        log = []
        ability = player["abilities"][ability_id]
        log.append(self._use_ability(player, player["current_enemy"], ability))

        if player["current_enemy"]["current_hp"] <= 0:
            levelFlag = self.player_service.add_experience(
                player, player["current_enemy"]["xp_reward"]
            )

            log.append(f"{player['name']} defeated {player['current_enemy']['name']}")
            log.append(
                f"{player['name']} gained {player['current_enemy']['xp_reward']} experience"
            )
            if levelFlag:
                log.append(f"{player['name']} leveled up to level {player['level']}!")
            log.append("To start a combat, go to /combat/start")

            self.enemy_service.die(player)
            await self.player_service.update_player(player)
            return {"log": log}

        enemy_action = random.randint(1, 2)
        log.append(self._take_turn(player["current_enemy"], player, enemy_action))

        if player["current_hp"] <= 0:
            log.append(
                f"{player['name']} was defeated by {player['current_enemy']['name']}"
            )
            log.append("Game over")
            log.append("To start a combat, go to /combat/start")

            self.player_service.die(player)

        await self.player_service.update_player(player)
        return {"log": log}

    def _take_turn(self, entity: Entity, target: Entity, action: int):
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
        combat_logger.info(
            f"⚔️ {attacker['name']} deals {damage:.2f} damage to {target['name']}"
        )
        combat_logger.info(
            f"  {target['name']} HP: {target['current_hp']:.2f}/{target['max_hp']}"
        )
        return f"{attacker['name']} attacked {target['name']} for {damage:.2f} damage"

    def _defend(self, entity):
        entity["is_defending"] = True
        combat_logger.info(f"🛡️ {entity['name']} is defending")
        return f"{entity['name']} is defending"

    def _use_ability(self, entity, target, ability):
        if entity["current_mana"] < ability["mana_cost"]:
            combat_logger.warning(
                f"{entity['name']} doesn't have enough mana to use {ability['name']}"
            )
            return (
                f"{entity['name']} does not have enough mana to use {ability['name']}"
            )

        entity["current_mana"] -= ability["mana_cost"]
        damage_mitigation = (target["defense"]) / (target["defense"] + 5)
        extra_mitigation = 0.3 if target.get("is_defending", False) else 0
        damage = ability["damage"] * (1 - damage_mitigation) * (1 - extra_mitigation)
        target["current_hp"] -= damage
        target["is_defending"] = False

        combat_logger.info(
            f"✨ {entity['name']} uses {ability['name']} on {target['name']} for {damage:.2f} damage"
        )
        combat_logger.info(
            f"  {target['name']} HP: {target['current_hp']:.2f}/{target['max_hp']}"
        )
        combat_logger.info(
            f"  {entity['name']} Mana: {entity['current_mana']}/{entity['max_mana']}"
        )
        return f"{entity['name']} used {ability['name']} on {target['name']} for {damage:.2f} damage"

    @staticmethod
    def attack(attacker, defender):
        damage = max(0, attacker.attack - defender.defense)
        defender.current_hp -= damage
        combat_logger.info(
            f"{attacker.name} attacks {defender.name} for {damage} damage"
        )
        if defender.current_hp <= 0:
            combat_logger.info(f"{defender.name} has been defeated!")
        return damage
