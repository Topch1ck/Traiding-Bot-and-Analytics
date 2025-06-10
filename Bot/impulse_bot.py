import os
import asyncio
import aiohttp
import numpy as np
import pandas as pd
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime
from dotenv import load_dotenv

# Загрузка из корня проекта
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# === Load environment variables ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_API")
CHAT_ID = int(os.getenv("CHAT_ID"))

# === Configuration ===
SYMBOLS = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "XRPUSDT", "XLMUSDT", "SOLUSDT"]
WINDOW = 20  # in candles
IMPULSE_THRESHOLD = 0.02  # 2%
TP_PCT = 0.01 / 100 # take profit 1%
SL_PCT = 99.0  # 99% stop loss
FETCH_INTERVAL = 60  # seconds
KLINE_LIMIT = 100

# === State ===
active_trades = {symbol: None for symbol in SYMBOLS}
cash = {symbol: 10.0 for symbol in SYMBOLS}

# === Bot ===
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# === Fetch klines ===
async def fetch_klines(session, symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit={KLINE_LIMIT}"
    async with session.get(url) as resp:
        data = await resp.json()
        return symbol, data

# === Check strategy ===
async def check_strategy(session, symbol):
    global cash
    symbol, klines = await fetch_klines(session, symbol)
    closes = np.array([float(k[4]) for k in klines])
    highs = np.array([float(k[2]) for k in klines])
    lows = np.array([float(k[3]) for k in klines])
    times = [datetime.utcfromtimestamp(int(k[0]) // 1000) for k in klines]

    rolling_max = pd.Series(closes).rolling(window=WINDOW).max().to_numpy()
    rolling_min = pd.Series(closes).rolling(window=WINDOW).min().to_numpy()
    drawdowns = (rolling_min / rolling_max - 1) * 100
    impulse_mask = drawdowns <= -IMPULSE_THRESHOLD

    if active_trades[symbol] is None:
        for i in range(WINDOW, len(closes)):
            if impulse_mask[i]:
                entry_price = closes[i]
                entry_time = times[i]
                tp = entry_price * (1 + TP_PCT)
                sl = entry_price * (1 - SL_PCT / 100)

                active_trades[symbol] = {
                    "entry_price": entry_price,
                    "entry_time": entry_time,
                    "take_profit": tp,
                    "stop_loss": sl
                }

                msg = (
                    f"📉 <b>Сигнал на вход (🟢Лонг)</b>\n\n"
                    f"🕒 <b>Время:</b> {entry_time.strftime('%d-%m-%Y %H:%M:%S')} UTC\n"
                    f"💱 <b>Валюта:</b> {symbol.replace('USDT', '')}/USDT\n"
                    f"💵 <b>Цена входа:</b> {entry_price:.4f}\n"
                    f"🎯 <b>TP:</b> {tp:.4f} ({TP_PCT:.2f}%)\n"
                    f"💰 <b>Cash:</b> ${cash[symbol]:.2f}"
                )
                await bot.send_message(CHAT_ID, msg, parse_mode="HTML")
                break
    else:
        trade = active_trades[symbol]
        for i in range(WINDOW, len(closes)):
            if highs[i] >= trade["take_profit"] or lows[i] <= trade["stop_loss"]:
                exit_price = trade["take_profit"] if highs[i] >= trade["take_profit"] else trade["stop_loss"]
                exit_time = times[i]
                profit_pct = (exit_price / entry_price - 1)
                cash_after = cash * (1 + profit_pct)
                profit_usdt = cash_after - cash

                duration_minutes = int((exit_time - entry_time).total_seconds() // 60)
                duration_str = f"{duration_minutes // 60}:{duration_minutes % 60:02d} ч"

                msg = f"""
                ✅ <b>Выход из сделки</b>

                🕐 <b>Вход:</b> {entry_time.strftime('%d-%m-%Y %H:%M:%S')} UTC
                🕐 <b>Выход:</b> {exit_time.strftime('%d-%m-%Y %H:%M:%S')} UTC
                ⏳ <b>Длительность:</b> {duration_str}

                💰 <b>Валюта:</b> {symbol}
                📉 <b>Цена входа:</b> {entry_price}
                📈 <b>Цена выхода:</b> {exit_price}
                🎯 <b>TP:</b> {profit_pct:.2%}
                📊 <b>Cash:</b> ${cash_after:.4f}
                💵 <b>Прибыль:</b> +${profit_usdt:.4f}
                """
                await bot.send_message(CHAT_ID, msg, parse_mode="HTML")
                active_trades[symbol] = None
                break

# === Main loop ===
async def main_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await asyncio.gather(*(check_strategy(session, symbol) for symbol in SYMBOLS))
                await asyncio.sleep(FETCH_INTERVAL)
            except Exception as e:
                await bot.send_message(CHAT_ID, f"❌ Ошибка: {e}")

# === Start bot ===
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())
    executor.start_polling(dp, skip_updates=True)
