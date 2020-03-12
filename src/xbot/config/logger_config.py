import sys

from flask import Flask
from flask_loguru import Logger
from loguru import logger

from xbot.properties import LOGGER_PATH, LOGGER_FILE, LOGGER_LEVEL


def init_logger(app: Flask):
    logger.remove()
    logger.add(sys.stdout, level=LOGGER_LEVEL)

    log = Logger()
    log.init_app(app, {
        "LOG_PATH": LOGGER_PATH,
        "LOG_NAME": LOGGER_FILE,
        "LOG_FORMAT": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> <level>{level}</level> {message}"
    })
