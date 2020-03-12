from flask_loguru import logger

from xbot.app import app
from xbot.properties import BOT_FACE
from xbot.service import bot_service


@app.route('/trigger')
def trigger():
    logger.info('{} Trigger controller is running...', BOT_FACE)

    bot_service.generate_csv_stock()

    return '{} Finish flow'.format(BOT_FACE)
