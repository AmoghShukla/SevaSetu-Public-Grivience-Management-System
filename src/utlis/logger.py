import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)

    if not logger.hasHandlers():
        if not os.path.exists('src/logs'):
            os.mkdir('src/logs/app.log')

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

        ConsoleHandler = logging.StreamHandler()
        ConsoleHandler.setFormatter(formatter)

        FileHandler = logging.FileHandler('src/logs/app.log')
        FileHandler.setFormatter(formatter)

        logger.addHandler(ConsoleHandler)
        logger.addHandler(FileHandler)
    
    return logger