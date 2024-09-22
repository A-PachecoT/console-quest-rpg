import random
from typing import List, Tuple

class DungeonService:
    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.dungeon: List[List[str]] = []

    def generate_dungeon(self) -> List[List[str]]:
        self.dungeon = [['#' for _ in range(self.width)] for _ in range(self.height)]
        
        # Create rooms
        for _ in range(5):  # Generate 5 rooms
            room_width = random.randint(3, 5)
            room_height = random.randint(3, 5)
            x = random.randint(1, self.width - room_width - 1)
            y = random.randint(1, self.height - room_height - 1)
            
            for i in range(y, y + room_height):
                for j in range(x, x + room_width):
                    self.dungeon[i][j] = '.'
        
        # Place entrance and exit
        self.place_entrance_and_exit()
        
        return self.dungeon

    def place_entrance_and_exit(self):
        empty_cells = [(i, j) for i in range(self.height) for j in range(self.width) if self.dungeon[i][j] == '.']
        if len(empty_cells) >= 2:
            entrance, exit = random.sample(empty_cells, 2)
            self.dungeon[entrance[0]][entrance[1]] = 'E'
            self.dungeon[exit[0]][exit[1]] = 'X'

    def get_player_position(self) -> Tuple[int, int]:
        for i in range(self.height):
            for j in range(self.width):
                if self.dungeon[i][j] == 'E':
                    return i, j
        return -1, -1  # Should never happen if dungeon is properly generated

    def move_player(self, direction: str) -> bool:
        y, x = self.get_player_position()
        new_y, new_x = y, x

        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1

        if 0 <= new_y < self.height and 0 <= new_x < self.width and self.dungeon[new_y][new_x] != '#':
            self.dungeon[y][x] = '.'
            self.dungeon[new_y][new_x] = 'E'
            return True
        return False