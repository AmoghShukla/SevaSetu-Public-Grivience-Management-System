import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)

    if not logger.hasHandlers():
        if not os.path.exists('src/logs'):
            os.mkdir('src/logs')

            
    