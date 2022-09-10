import requests
import os


class TelegramConnector:
    token: str
    chatId: str

    def __init__(self):
        self.token = os.getenv('REMIND_THEM_TOKEN')
        self.chatId = os.getenv('REMIND_THEM_CHAT_ID')

        if self.token == None:
            raise Exception("Missing environment variable REMIND_THEM_TOKEN with Telegram token")

        if self.chatId == None:
            raise Exception("Missing environment variable REMIND_THEM_CHAT_ID with Telegram chat ID")


    def message_sender(self, message):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatId + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)
        return response.json()


test = TelegramConnector()
test.message_sender("PROBANDO PROBANDO")
