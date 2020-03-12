from flask import Flask

from xbot.config.logger_config import init_logger

app = Flask(__name__)

init_logger(app)

from xbot.controller import trigger_controller
from xbot.controller import health_controller

if __name__ == '__main__':
    app.run(debug=True)
