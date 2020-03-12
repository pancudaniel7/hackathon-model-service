import os

get = os.environ.get

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

APP_NAME = get("APP_NAME", default="x-bot")
BOT_FACE = get("BOT_LOG", default="d[x_x]b")

CSV_DIR = ROOT_DIR + '/resources/csv/'
CSV_BLACK_FILE_PATH = CSV_DIR + 'blank.csv'
CSV_STOCK_FILE_PATH = os.environ['HOME'] + '/csv/stock.csv'

FIREFOX_HEADLESS = get("FIREFOX_HEADLESS", default="true")

TARGET_LOGIN_URL = get("TARGET_LOGIN_URL", default="http://pieseauto.ro/autentificare/")
TARGET_STOCK_URL = get("TARGET_STOCK_URL", default="https://www.pieseauto.ro/sales.php?action=management")

VAULT_TOKEN = get("VAULT_TOKEN")
VAULT_ADDRESS = get("VAULT_ADDRESS", default="http://localhost:8200")
VAULT_X_BOT_SECRET_PATH = get("VAULT_X_BOT_SECRET_PATH", default="xbot")

LOGGER_PATH = get("LOGGER_PATH", default="/var/log/")
LOGGER_FILE = get("LOGGER_FILE", default=APP_NAME + ".log")
LOGGER_LEVEL = get("LOGGER_LEVEL", default='INFO')
