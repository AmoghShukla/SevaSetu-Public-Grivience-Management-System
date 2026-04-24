import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)
    