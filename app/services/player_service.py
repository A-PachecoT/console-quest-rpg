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

    async def create_player(self, name: str):
        """
        Crea un nuevo jugador.

        Args:
            player (Player): El jugador a crear.

        Returns:
            str: El ID del jugador creado.
        """
        player = Player(name=name)
        return await self.player_queries.create_player(player)

    async def get_player(self, player_id: str) -> Player:
        """
        Obtiene un jugador por su ID.

        Args:
            player_id (str): El ID del jugador a obtener.

        Returns:
            Player: El jugador encontrado.
        """
        return await self.player_queries.get_player(player_id)

    async def get_all_players(self) -> list[Player]:
        """
        Obtiene todos los jugadores.

        Returns:
            list[Player]: Lista de todos los jugadores.
        """
        return await self.player_queries.get_all_players()

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
