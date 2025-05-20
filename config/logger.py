# config/logger.py

import logging
import sys
from colorlog import ColoredFormatter

LOG_FILE = "logs/weather_pipeline.log"

def get_logger(name: str) -> logging.Logger:
    """Returns a logger with both console (colored) and file output."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers during re-import
    if logger.hasHandlers():
        return logger

    # Formatter for console (colored)
    color_formatter = ColoredFormatter(
        "%(log_color)s[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(color_formatter)
    logger.addHandler(console_handler)

    # File handler
    file_formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger
