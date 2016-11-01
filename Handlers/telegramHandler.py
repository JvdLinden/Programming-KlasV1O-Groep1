import telepot

CODE_HEADER_REGISTER = '#'

class TelegramHandler(object):
    """This class will handle all interaction with our telegram bot.

    """

    def __init__(self, token, current_response):
        self.bot = telepot.Bot(token)
        self.current_response = current_response

    def getCurrentUpdateNr(self):
        """returns the current update_id

        """
        return self.current_response

    def sendMessageToUser(self, chat_id, message):
        """Sends a message to a given user

        """
        #Attempt to send a message
        try:
            return self.bot.sendMessage(chat_id, message, parse_mode='Markdown')

        #Catch TelegramErrors (i.e. 'chat not found')
        except telepot.exception.TelegramError as error:
            return error

    def getNewUpdates(self):
        """returns all new updates

        """
        return self.bot.getUpdates(self.current_response+1)

    def getNextUpdate(self, current = 0):
        """Returns the next update from the bot (and will wait untill it receives one)

        """
        if current == 0:
            current = self.current_response + 1

        _update = None
        while _update == None:
            _update = self.bot.getUpdates(current, limit=1)

        return _update

    def handleUpdates(self, updates):
        """Handles all updates, and returns a list of dicts with update data

        """
        _list = []
        for update in updates:
            _list += [self.handleUpdate(update)]
        return _list

    def handleUpdate(self, update):
        """Handles a single update

        This is currently a test function, as we still have to vdevelop a format for passing and receiving codes.
        """
        if not update:
            return {}

        update_id = update['update_id']

        if self.current_response < update_id:
            self.current_response = update_id

        code = None
        message = update['message']
        text = message['text']

        if text.startswith(CODE_HEADER_REGISTER):
            code = text.strip(CODE_HEADER_REGISTER).split()[0]

        chat_id = message['chat']['id']

        return {
            'code': code,
            'id' :chat_id,
            'uid': update_id,
            'text':text
        }
