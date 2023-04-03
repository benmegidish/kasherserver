import requests
from dotenv import load_dotenv
import os

def newMessage(message):
    load_dotenv()
    chatId = os.getenv('telgramChatId')
    url = os.getenv('telgramBase_url')
    base_url = f'{url}{chatId}&text="{message}"'
    requests.get(base_url)
 