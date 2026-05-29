import logging
import os

def configurar_logger():
    nivel = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, nivel, logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("sentinela.log", encoding="utf-8"),
        ],
    )
    return logging.getLogger("sentinela")

logger = configurar_logger()