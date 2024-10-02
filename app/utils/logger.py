import logging
import colorlog
from logging.handlers import RotatingFileHandler
import os


class CustomFilter(logging.Filter):
    def filter(self, record):
        record.filename = record.filename.split(".")[0]  # Remove file extension
        return True


class MetricsFormatter(colorlog.ColoredFormatter):
    def format(self, record):
        if record.name == "metrics":
            # Use white color for metrics logs
            self.log_colors = {"INFO": "white"}
        else:
            # Use default colors for other logs
            self.log_colors = {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            }
        return super().format(record)


def setup_logger(name, log_file, level=logging.INFO):
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    formatter = MetricsFormatter(
        "%(log_color)s%(asctime)s | %(filename)s | %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler
    file_handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(filename)s | %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    # Console handler
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = colorlog.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Add custom filter
    custom_filter = CustomFilter()
    logger.addFilter(custom_filter)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


# Create loggers
main_logger = setup_logger("main", "/app/logs/main.log")
api_logger = setup_logger("api", "/app/logs/api.log")
db_logger = setup_logger("database", "/app/logs/database.log")
player_logger = setup_logger("player", "/app/logs/player.log")
monster_logger = setup_logger("monster", "/app/logs/monster.log")
combat_logger = setup_logger("combat", "/app/logs/combat.log")
metrics_logger = setup_logger("metrics", "/app/logs/metrics.log")

# Disable uvicorn access log
logging.getLogger("uvicorn.access").disabled = True
