# bot/bot.py
import os
import requests
from settings import Settings

def send_message(text):
    token = Settings.TELEGRAM_BOT_TOKEN
    chat_id = Settings.TELEGRAM_CHAT_ID

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}

    try:
        resp = requests.post(url, json=data)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")
