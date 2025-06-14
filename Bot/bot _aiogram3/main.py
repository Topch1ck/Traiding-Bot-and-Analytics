import os

from dotenv import load_dotenv

# Загрузка из корня проекта
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# === Load environment variables ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_API")
chat_id_str = os.getenv("CHAT_ID")
if chat_id_str is None:
    raise ValueError("Environment variable CHAT_ID is not set")

CHAT_ID: int = int(chat_id_str)

# === Configuration ===
SYMBOLS = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "XRPUSDT", "XLMUSDT", "SOLUSDT"]
WINDOW = 20  # in candles
IMPULSE_THRESHOLD = 0.02  # 2%
TP_PCT = 0.01 / 100  # take profit 1%
SL_PCT = 99.0  # 99% stop loss
FETCH_INTERVAL = 60  # seconds
KLINE_LIMIT = 100

# === State ===
active_trades = {symbol: None for symbol in SYMBOLS}
cash = {symbol: 10.0 for symbol in SYMBOLS}
