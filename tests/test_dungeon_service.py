import pytest
from app.services.dungeon_service import DungeonService

@pytest.fixture
def dungeon_service():
    return DungeonService(width=10, height=10)

def test_generate_dungeon(dungeon_service):
    dungeon = dungeon_service.generate_dungeon()
    assert len(dungeon) == 10
    assert len(dungeon[0]) == 10
    assert any('E' in row for row in dungeon)
    assert any('X' in row for row in dungeon)

def test_get_player_position(dungeon_service):
    dungeon_service.generate_dungeon()
    y, x = dungeon_service.get_player_position()
    assert dungeon_service.dungeon[y][x] == 'E'

def test_move_player(dungeon_service):
    dungeon_service.generate_dungeon()
    initial_y, initial_x = dungeon_service.get_player_position()
    
    # Try all directions
    directions = ['up', 'down', 'left', 'right']
    for direction in directions:
        result = dungeon_service.move_player(direction)
        new_y, new_x = dungeon_service.get_player_position()
        
        if result:
            assert dungeon_service.dungeon[new_y][new_x] == 'E'
            assert dungeon_service.dungeon[initial_y][initial_x] == '.'
            return  # If we successfully moved, end the test
    
    # If we couldn't move in any direction, the test should fail
    pytest.fail("Player couldn't move in any direction")