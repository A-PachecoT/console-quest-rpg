from typing import List
from ..models.character import Character
from ..models.monster import Monster
from random import randint

class CombatService:
    @staticmethod
    def initiate_combat(character: Character, monsters: List[Monster]):
        """
        Inicia un combate entre el personaje y una lista de monstruos.
        """
        combat_log = []
        combat_log.append(f"¡Combate iniciado! {character.name} vs {len(monsters)} monstruos")
        
        while character.current_hp > 0 and any(monster.current_hp > 0 for monster in monsters):
            # Turno del personaje
            combat_log.extend(CombatService._character_turn(character, monsters))
            
            # Turno de los monstruos
            for monster in monsters:
                if monster.current_hp > 0:
                    combat_log.extend(CombatService._monster_turn(monster, character))
            
            # Verificar si el combate ha terminado
            if character.current_hp <= 0:
                combat_log.append(f"{character.name} ha sido derrotado.")
                break
            elif all(monster.current_hp <= 0 for monster in monsters):
                combat_log.append("¡Todos los monstruos han sido derrotados!")
                break
        
        return combat_log

    @staticmethod
    def _character_turn(character: Character, monsters: List[Monster]) -> List[str]:
        """
        Ejecuta el turno del personaje.
        """
        log = []
        target = next((monster for monster in monsters if monster.current_hp > 0), None)
        if target:
            damage = max(1, character.attack - target.defense)
            target.current_hp = max(0, target.current_hp - damage)
            log.append(f"{character.name} ataca a {target.name} causando {damage} de daño.")
            if target.current_hp == 0:
                log.append(f"{target.name} ha sido derrotado.")
        return log

    @staticmethod
    def _monster_turn(monster: Monster, character: Character) -> List[str]:
        """
        Ejecuta el turno de un monstruo.
        """
        log = []
        if monster.current_hp > 0:
            damage = max(1, monster.attack - character.defense)
            character.current_hp = max(0, character.current_hp - damage)
            log.append(f"{monster.name} ataca a {character.name} causando {damage} de daño.")
        return log

    @staticmethod
    def calculate_rewards(character: Character, defeated_monsters: List[Monster]):
        """
        Calcula la experiencia y el oro ganados después del combate.
        """
        total_xp = sum(monster.xp_reward for monster in defeated_monsters)
        total_gold = sum(monster.gold_reward for monster in defeated_monsters)
        
        character.xp += total_xp
        character.gold += total_gold
        
        return total_xp, total_gold