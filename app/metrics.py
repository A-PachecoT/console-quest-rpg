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
    def instrumentation(info: metrics.Info) -> None:
        pass

    return instrumentation


def player_level_metric() -> Callable[[metrics.Info], None]:
    def instrumentation(info: metrics.Info) -> None:
        pass

    return instrumentation


def combat_outcomes_metric() -> Callable[[metrics.Info], None]:
    def instrumentation(info: metrics.Info) -> None:
        pass

    return instrumentation
