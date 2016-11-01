import telepot

CODE_HEADER_REGISTER = '#'

class TelegramHandler(object):

    def __init__(self, token, current_response):
        self.bot = telepot.Bot(token)
        self.current_response = current_response

    def sendMessageToUser(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)

    def getNewUpdates(self):
        return self.bot.getUpdates(self.current_response+1)

    def getNextUpdate(self):
        return self.bot.getUpdates(self.current_response+1,limit=1)

    def handleUpdates(self, updates):
        _list = []
        for update in updates:
            _list += [self.handleUpdate(update)]
        return _list

    def handleUpdate(self, update):
        if not update:
            return 0

        message = update['message']

        text = message['text']
        first_name = message['chat']['first_name']

        update_id = update['update_id']
        chat_id = message['chat']['id']

        if self.current_response < update_id:
            self.current_response = update_id

        if text.startswith(CODE_HEADER_REGISTER):

            code = text.strip(CODE_HEADER_REGISTER)

            return {'code': code, 'id':chat_id}
        return None
