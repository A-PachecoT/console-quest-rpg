from app.models.player import Player
from app.database.mongo.queries.player import PlayerQueries

class PlayerService:
    def __init__(self, player_queries: PlayerQueries):
        self.player_queries = player_queries

    async def create_player(self, player: Player) -> str:
        return await self.player_queries.create_player(player)

    async def get_player(self, player_id: str) -> Player:
        return await self.player_queries.get_player(player_id)

    async def get_all_players(self) -> list[Player]:
        return await self.player_queries.get_all_players()

    async def update_player(self, player_id: str, player: Player) -> bool:
        return await self.player_queries.update_player(player_id, player)

    async def delete_player(self, player_id: str) -> bool:
        return await self.player_queries.delete_player(player_id)
