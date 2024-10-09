from prometheus_client import Counter, Gauge

# Define custom Prometheus metrics
PLAYER_DAMAGE = Counter(
    "player_damage_total", "Total damage dealt by player", ["player_name"]
)
PLAYER_LEVEL = Gauge("player_level", "Current player level", ["player_name"])
COMBAT_OUTCOMES = Counter(
    "combat_outcomes_total", "Total combat outcomes", ["player_name", "outcome"]
)
