import requests

from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_URL


def send_tg_message(chat_id, message):
    """Sends message to Telegram chat"""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
