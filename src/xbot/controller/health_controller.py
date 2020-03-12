from xbot.app import app
from xbot.properties import BOT_FACE


@app.route('/health')
def hello_world():
    app.init_logger.info('{} The service is Up and Running!', BOT_FACE)
    return 'up'
