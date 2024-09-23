from typing import List, Dict
from ..models.character import Character
from ..models.monster import Monster
from random import randint

class CombatService:
    combats: Dict[str, Dict] = {}

    @staticmethod
    def initiate_combat(combat_id: str, character: Character, monsters: List[Monster]):
        """
        Inicia un combate entre el personaje y una lista de monstruos.
        """
        CombatService.combats[combat_id] = {
            "character": character,
            "monsters": monsters,
            "log": [f"¡Combate iniciado! {character.name} vs {len(monsters)} monstruos"]
        }

    @staticmethod
    def character_turn(combat_id: str, action: str, target_index: int):
        """
        Ejecuta el turno del personaje.
        """
        combat = CombatService.combats.get(combat_id)
        if not combat:
            return ["Combate no encontrado"]

        character = combat["character"]
        monsters = combat["monsters"]
        log = combat["log"]

        if target_index < 0 or target_index >= len(monsters):
            return ["Índice de objetivo inválido"]

        target = monsters[target_index]
        if target.current_hp <= 0:
            return ["El objetivo ya está derrotado"]

        if action == "basic_attack":
            damage = CombatService._calculate_damage(character.attack, target.defense)
            target.current_hp = max(0, target.current_hp - damage)
            log.append(f"{character.name} realiza un ataque básico a {target.name} causando {damage} de daño.")
        else:  # Uso de habilidad
            skill_damage, skill_effect = CombatService._use_skill(character, action)
            damage = CombatService._calculate_damage(skill_damage, target.defense)
            target.current_hp = max(0, target.current_hp - damage)
            log.append(f"{character.name} usa {action} contra {target.name} causando {damage} de daño.")
            if skill_effect:
                log.append(f"Efecto adicional: {skill_effect}")

        if target.current_hp == 0:
            log.append(f"{target.name} ha sido derrotado.")

        return log

    @staticmethod
    def monster_turn(combat_id: str):
        """
        Ejecuta el turno de los monstruos.
        """
        combat = CombatService.combats.get(combat_id)
        if not combat:
            return ["Combate no encontrado"]

        character = combat["character"]
        monsters = combat["monsters"]
        log = combat["log"]

        for monster in monsters:
            if monster.current_hp > 0:
                damage = CombatService._calculate_damage(monster.attack, character.defense)
                character.current_hp = max(0, character.current_hp - damage)
                log.append(f"{monster.name} ataca a {character.name} causando {damage} de daño.")

        if character.current_hp <= 0:
            log.append(f"{character.name} ha sido derrotado.")

        return log

    @staticmethod
    def _calculate_damage(attack: int, defense: int) -> int:
        """
        Calcula el daño basado en el ataque y la defensa.
        """
        base_damage = max(1, attack - defense)
        variance = randint(-2, 2)  # Añade un poco de variabilidad al daño
        return max(1, base_damage + variance)

    @staticmethod
    def _use_skill(character: Character, skill_name: str) -> tuple:
        """
        Usa una habilidad del personaje.
        """
        # Aquí se implementaría la lógica de las habilidades
        # Por ahora, retornamos valores de ejemplo
        if skill_name == "fireball":
            return (character.attack * 1.5, "El objetivo está quemado")
        elif skill_name == "ice_shard":
            return (character.attack * 1.2, "El objetivo está congelado")
        else:
            return (character.attack, None)

    @staticmethod
    def get_combat_log(combat_id: str) -> List[str]:
        """
        Obtiene el registro del combate.
        """
        combat = CombatService.combats.get(combat_id)
        if not combat:
            return ["Combate no encontrado"]
        return combat["log"]