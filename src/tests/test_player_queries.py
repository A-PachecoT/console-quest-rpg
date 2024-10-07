import pytest
from app.models.player import Player
from unittest.mock import AsyncMock
from bson import ObjectId


@pytest.mark.asyncio
async def test_register(player_queries, mock_db):
    player = Player(name="TestPlayer", password="testpass")
    mock_db.players.insert_one.return_value = AsyncMock(inserted_id="some_id")
    result = await player_queries.register(player)
    assert result["message"] == "Player created successfully"
    assert result["player"] == "TestPlayer"


@pytest.mark.asyncio
async def test_login(player_queries, mock_db):
    mock_db.players.find_one.return_value = {
        "_id": ObjectId("60d5ec49f1b2c8b1f8e4e1a1"),
        "name": "TestPlayer",
        "password": "hashed_password",
    }
    result = await player_queries.login("TestPlayer")
    assert result["message"] == "Login successful"
    assert "password" in result


@pytest.mark.asyncio
async def test_get_player_by_name(player_queries, mock_db):
    mock_db.players.find_one.return_value = {
        "_id": ObjectId("60d5ec49f1b2c8b1f8e4e1a1"),
        "name": "TestPlayer",
        "password": "hashed_password",
    }
    result = await player_queries.get_player_by_name("TestPlayer")
    assert result["message"] == "Player retrieved successfully"
    assert result["player"]["name"] == "TestPlayer"


# Implementar esta prueba
# @pytest.mark.asyncio
# async def test_get_all_players(player_queries, mock_db):


@pytest.mark.asyncio
async def test_update_player(player_queries, mock_db):
    player_data = {
        "_id": "60d5ec49f1b2c8b1f8e4e1a1",
        "name": "UpdatedPlayer",
        "password": "new_password",
    }
    mock_db.players.update_one.return_value = AsyncMock(modified_count=1)
    result = await player_queries.update_player(player_data)
    assert result is True


@pytest.mark.asyncio
async def test_delete_player(player_queries, mock_db):
    mock_db.players.delete_one.return_value = AsyncMock(deleted_count=1)
    result = await player_queries.delete_player("60d5ec49f1b2c8b1f8e4e1a1")
    assert result is True


@pytest.mark.asyncio
async def test_delete_all_players(player_queries, mock_db):
    mock_db.players.delete_many.return_value = AsyncMock(deleted_count=5)
    result = await player_queries.delete_all_players()
    assert result["message"] == "All players deleted successfully"
    assert result["deleted_count"] == 5


@pytest.mark.asyncio
async def test_it_exists(player_queries, mock_db):
    mock_db.players.find_one.return_value = {
        "_id": ObjectId("60d5ec49f1b2c8b1f8e4e1a1"),
        "name": "TestPlayer",
    }
    exists = await player_queries.it_exists("TestPlayer")
    assert exists is True

    mock_db.players.find_one.return_value = None
    exists = await player_queries.it_exists("NonExistentPlayer")
    assert exists is False
