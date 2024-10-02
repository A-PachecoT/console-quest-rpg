import logging
import colorlog
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file, level=logging.INFO):
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)s %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )

    # File handler
    file_handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    )

    # Console handler
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = colorlog.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Create loggers
main_logger = setup_logger("main", "logs/main.log")
api_logger = setup_logger("api", "logs/api.log")
db_logger = setup_logger("database", "logs/database.log")
