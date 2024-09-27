from app.models.player import Player
from app.database.mongo.queries.player import PlayerQueries

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

    async def create_player(self, name: str) ->dict:
        """
        Crea un nuevo jugador.

        Args:
            player (Player): El jugador a crear.

        Returns:
            str: El ID del jugador creado.
        """
        if await self.player_queries.get_player(name):
            return {
                "message": "Player already exists"
            }

        player = Player(name=name)
        return await self.player_queries.create_player(player)
    
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
