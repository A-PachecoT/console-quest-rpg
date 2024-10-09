import pytest
from unittest.mock import AsyncMock
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database.mongo.queries.player import PlayerQueries
from app.services.player_service import PlayerService


@pytest.fixture(scope="module")
def mock_db():
    mock_db = AsyncMock(spec=AsyncIOMotorDatabase)
    mock_collection = AsyncMock()
    mock_db.players = mock_collection
    return mock_db


@pytest.fixture(scope="module")
def player_queries(mock_db):
    return PlayerQueries(mock_db)


@pytest.fixture(scope="module")
def player_service(player_queries):
    return PlayerService(player_queries)
