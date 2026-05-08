import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)

    if not logger.hasHandlers():
        if not os.path.exists('src/logs/app/log'):
            os.makedirs('src/logs/app.log')

        formatter = logging.Formatter('  %(asctimes)s | %(levelname)s | %(name)s | %(message)s')

        ConsoleHandler = logging.StreamHandler()
        ConsoleHandler.setFormatter(formatter)

        FileHandler = logging.FileHandler()
        FileHandler.setFormatter(formatter)

        logger.addHandler(ConsoleHandler)
        logger.addHandler(FileHandler)
    
    return logger