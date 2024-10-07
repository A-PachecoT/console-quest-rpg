from prometheus_client import Counter, Gauge
from typing import Callable
from prometheus_fastapi_instrumentator import metrics

# Define custom Prometheus metrics
PLAYER_DAMAGE = Counter(
    "player_damage_total", "Total damage dealt by player", ["player_name"]
)
PLAYER_LEVEL = Gauge("player_level", "Current player level", ["player_name"])
COMBAT_OUTCOMES = Counter(
    "combat_outcomes_total", "Total combat outcomes", ["player_name", "outcome"]
)


def player_damage_metric() -> Callable[[metrics.Info], None]:
    """
    Función que retorna un callable para instrumentar la métrica de daño del jugador.

    Returns:
        Callable[[metrics.Info], None]: Una función de instrumentación para la métrica de daño del jugador.
    """

    def instrumentation(info: metrics.Info) -> None:
        """
        Función de instrumentación para la métrica de daño del jugador.
        Actualmente no implementada.

        Args:
            info (metrics.Info): Información de la métrica.
        """
        pass

    return instrumentation


def player_level_metric() -> Callable[[metrics.Info], None]:
    """
    Función que retorna un callable para instrumentar la métrica de nivel del jugador.

    Returns:
        Callable[[metrics.Info], None]: Una función de instrumentación para la métrica de nivel del jugador.
    """

    def instrumentation(info: metrics.Info) -> None:
        """
        Función de instrumentación para la métrica de nivel del jugador.
        Actualmente no implementada.

        Args:
            info (metrics.Info): Información de la métrica.
        """
        pass

    return instrumentation


def combat_outcomes_metric() -> Callable[[metrics.Info], None]:
    """
    Función que retorna un callable para instrumentar la métrica de resultados de combate.

    Returns:
        Callable[[metrics.Info], None]: Una función de instrumentación para la métrica de resultados de combate.
    """

    def instrumentation(info: metrics.Info) -> None:
        """
        Función de instrumentación para la métrica de resultados de combate.
        Actualmente no implementada.

        Args:
            info (metrics.Info): Información de la métrica.
        """
        pass

    return instrumentation
