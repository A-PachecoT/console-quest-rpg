from models.character import Character
from typing import List, Optional

class CharacterService:
    def __init__(self):
        self.characters: List[Character] = []

    def create_character(self, character: Character) -> Character:
        character.id = len(self.characters) + 1
        self.characters.append(character)
        return character

    def get_character(self, character_id: int) -> Optional[Character]:
        for character in self.characters:
            if character.id == character_id:
                return character
        return None

    def update_character(self, character_id: int, updated_character: Character) -> Optional[Character]:
        for i, character in enumerate(self.characters):
            if character.id == character_id:
                updated_character.id = character_id
                self.characters[i] = updated_character
                return updated_character
        return None

    def delete_character(self, character_id: int) -> bool:
        for i, character in enumerate(self.characters):
            if character.id == character_id:
                del self.characters[i]
                return True
        return False

    def level_up(self, character_id: int) -> Optional[Character]:
        character = self.get_character(character_id)
        if character:
            character.level += 1
            character.max_hp += 10
            character.hp = character.max_hp
            character.attack += 2
            character.defense += 1
            return character
        return None