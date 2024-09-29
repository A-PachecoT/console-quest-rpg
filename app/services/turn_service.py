class TurnService:
    @staticmethod
    def attack(attacker, target):
        damage_mitigation = (target.defense) / (target.defense + 5)
        extra_mitigation = 0.3 if target.is_defendig else 0
        damage = attacker.attack * (1 - damage_mitigation) * (1 - extra_mitigation)
        target.current_hp -= damage
        target.is_defendig = False
        return f"{attacker.name} attacked {target.name} for {damage} damage"

    @staticmethod
    def defend(entity):
        entity.is_defendig = True
        return f"{entity.name} is defending"

    @staticmethod
    def take_turn(entity, target, action: int):
        if action == 1:
            return TurnService.attack(entity, target)
        if action == 2:
            return TurnService.defend(entity)
        return "Invalid action"
