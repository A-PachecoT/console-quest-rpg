from bson import ObjectId
from typing import List
from app.models.player import Player
from pymongo.database import Database

class PlayerQueries:
    def __init__(self, db: Database):
        self.collection = db.players

    async def create_player(self, player: Player) -> str:
        player_dict = player.dict(exclude={"id"}, by_alias=True)
        result = await self.collection.insert_one(player_dict)
        return str(result.inserted_id)

    async def get_player(self, player_id: str) -> Player:
        player_data = await self.collection.find_one({"_id": ObjectId(player_id)})
        if player_data:
            player_data["_id"] = str(player_data["_id"])
            return Player(**player_data)
        return None

    async def get_all_players(self) -> List[Player]:
        cursor = self.collection.find()
        players = []
        async for player_data in cursor:
            player_data["_id"] = str(player_data["_id"])
            players.append(Player(**player_data))
        return players

    async def update_player(self, player_id: str, player: Player) -> bool:
        update_data = player.dict(exclude={"id"}, exclude_unset=True)
        result = await self.collection.update_one(
            {"_id": ObjectId(player_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    async def delete_player(self, player_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(player_id)})
        return result.deleted_count > 0