import logging
from logging.handlers import RotatingFileHandler

from config.settings import LOG_DIR


LOG_FILE = LOG_DIR / "framework.log"


def setup_logger():

    logger = logging.getLogger("AIRecon")

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,
        backupCount=3
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()