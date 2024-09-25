from bson import ObjectId
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.player import Player
from pymongo.database import Database

class PlayerQueries:
	"""
	Clase para interactuar con la colección de jugadores en la base de datos.
	"""
	def __init__(self, db: Database):
		"""
		Inicializa la instancia con la base de datos y la colección de jugadores.

		Args:
			db (Database): Instancia de la base de datos MongoDB.
		"""
		self.collection = db.players

	async def create_player(self, player: Player):
		"""
		Crea un nuevo jugador en la base de datos.

		Args:
			player (Player): Objeto Player con los datos del jugador a crear.

		Returns:
			JSONResponse: Respuesta JSON con un mensaje y los datos del jugador creado.
		"""
		try:
			player_dict = player.model_dump()
			result = await self.collection.insert_one(player_dict)
			player_dict["_id"] = str(result.inserted_id)
			
			return JSONResponse(content=jsonable_encoder({
				"message": "Player created successfully",
				"player": player_dict
			})) 
		except Exception as e:
			print(e)
			return JSONResponse(content=jsonable_encoder({
				"message": "An error occurred while creating the player"
			}), status_code=500)


	async def get_player(self, player_id: str) -> Player:
		"""
		Obtiene un jugador por su ID.

		Args:
			player_id (str): ID del jugador a buscar.

		Returns:
			Player: Objeto Player con los datos del jugador encontrado, o None si no se encuentra.
		"""
		player_data = await self.collection.find_one({"_id": ObjectId(player_id)})
		if player_data:
			player_data["_id"] = str(player_data["_id"])
			return player_data
		return None

	async def get_all_players(self) -> List[Player]:
		"""
		Obtiene todos los jugadores.

		Returns:
			List[Player]: Lista de objetos Player con los datos de todos los jugadores.
		"""
		cursor = self.collection.find()
		players = []
		async for player_data in cursor:
			player_data["_id"] = str(player_data["_id"])
			players.append(Player(**player_data))
		return players

	async def update_player(self, player_id: str, player: Player) -> bool:
		"""
		Actualiza los datos de un jugador.

		Args:
			player_id (str): ID del jugador a actualizar.
			player (Player): Objeto Player con los nuevos datos del jugador.

		Returns:
			bool: True si se actualizó correctamente, False en caso contrario.
		"""
		update_data = player.dict(exclude={"id"}, exclude_unset=True)
		result = await self.collection.update_one(
			{"_id": ObjectId(player_id)},
			{"$set": update_data}
		)
		return result.modified_count > 0

	async def delete_player(self, player_id: str) -> bool:
		"""
		Elimina un jugador por su ID.

		Args:
			player_id (str): ID del jugador a eliminar.

		Returns:
			bool: True si se eliminó correctamente, False en caso contrario.
		"""
		result = await self.collection.delete_one({"_id": ObjectId(player_id)})
		return result.deleted_count > 0