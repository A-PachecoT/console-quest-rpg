from app.models.player import Player
from app.database.mongo.queries.player import PlayerQueries
import jwt
import bcrypt
import datetime
from app.config import settings

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
SALT_ROUNDS = settings.SALT_ROUNDS


class PlayerService:
    """
    Servicio para manejar operaciones relacionadas con los jugadores.
    """

    def __init__(self, player_queries: PlayerQueries):
        """
        Inicializa el servicio de jugadores.

        Args:
            player_queries (PlayerQueries): Instancia de las consultas de jugadores.
        """
        self.player_queries = player_queries

    async def register(self, name: str, password: str) -> dict:
        """
        Crea un nuevo jugador.

        Args:
            player (Player): El jugador a crear.

        Returns:
            str: El ID del jugador creado.
        """
        if await self.player_queries.it_exists(name):
            raise Exception("Player already exists")

        player = Player(name=name, password=password)
        try:
            result = await self.player_queries.register(player)
            if "player" in result:
                player_name = result["player"]
                token = jwt.encode(
                    {
                        "name": player_name,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                    },
                    JWT_SECRET_KEY,
                    algorithm="HS256",
                )
                response = {"message": "Registration successful", "token": token}
                return response
            else:
                raise Exception("An error occurred while creating the player")
        except Exception as e:
            raise Exception(e)

    async def login(self, name: str, password: str) -> dict:
        """
        Inicia sesión de un jugador.

        Args:
            name (str): El nombre del jugador.
            password (str): La contraseña del jugador.

        Returns:
            dict: Un diccionario con el mensaje de inicio de sesión.
        """
        if not await self.player_queries.it_exists(name):
            raise Exception("Player not found, please register in /register")

        player = await self.player_queries.get_player_get_by_name(name)
        try:
            isValid = bcrypt.checkpw(
                password.encode("utf-8"), player["player"]["password"].encode("utf-8")
            )
            if not isValid:
                raise Exception("Invalid password")
        except Exception as e:
            raise Exception(f"An error occurred while checking passwords: {e}")

        try:
            token = jwt.encode(
                {
                    "name": name,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                },
                JWT_SECRET_KEY,
                algorithm="HS256",
            )
            return {"message": "Login successful", "token": token}
        except Exception as e:
            raise Exception("An error occurred while logging in")

    async def get_all_players(self) -> dict:
        return await self.player_queries.get_all_players()

    async def get_player_get_by_name(self, player_name: str) -> dict:
        return await self.player_queries.get_player_get_by_name(player_name)

    async def update_player(self, player_id: str, player: Player) -> bool:
        """
        Actualiza un jugador existente.

        Args:
            player_id (str): El ID del jugador a actualizar.
            player (Player): Los nuevos datos del jugador.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """
        return await self.player_queries.update_player(player_id, player)

    async def delete_player(self, player_id: str) -> bool:
        """
        Elimina un jugador.

        Args:
            player_id (str): El ID del jugador a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        return await self.player_queries.delete_player(player_id)
