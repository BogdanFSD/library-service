import requests
from django.conf import settings


def send_telegram_alert(message):
    token = settings.BOT_TOKEN
    chat_id = settings.CHAT_ID
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(base_url)
    return response.json()
