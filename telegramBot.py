import requests
# from dotenv import load_dotenv
# import os

def newMessage(message):
    telgramBase_url = 'https://api.telegram.org/bot6158076717:AAGA8WpqELARX4FZ4hYRavreTGy3pb3LjX8/sendMessage?chat_id='
    telgramChatId=-1001625035427
    telegramBotToken = '6158076717:AAGA8WpqELARX4FZ4hYRavreTGy3pb3LjX8'
    # load_dotenv()
    # chatId = os.getenv('telgramChatId')
    # url = os.getenv('telgramBase_url')
    chatId = telgramChatId
    url = telgramBase_url
    base_url = f'{url}{chatId}&text="{message}"'
    requests.get(base_url)
  