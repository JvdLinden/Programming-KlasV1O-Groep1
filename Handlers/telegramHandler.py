import telepot
import string, random
from ProjectData import Constants

CODE_HEADER_REGISTER = '#'

class TelegramHandler(object):
    """This class will handle all interaction with our telegram bot.

    """

    def __init__(self, token, current_response):
        self.bot = telepot.Bot(token)
        self.current_response = current_response

    def getCurrentUpdateNr(self):
        """Get the current update index

        :return: the index
        """
        return self.current_response

    def sendMessageToUser(self, chat_id, message):
        """Send a message to a user via the user's chatID

        :param chat_id: the chatID related to the user you wish to message
        :param message: the message that should be sent to the user
        :return: the message data or an error
        """
        #Attempt to send a message
        try:
            return self.bot.sendMessage(chat_id, message, parse_mode='Markdown')

        #Catch TelegramErrors (i.e. 'chat not found')
        except telepot.exception.TelegramError as error:
            return error

    def sendValidationCodeToUser(self, chatID):
        """This functions generates a validation code and sends it to the chat corresponding to the chatID.

        :param chatID: the chat ID related to the user we want to message
        :return: the code sent to the user
        """
        _code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Constants.LENGTH_VALIDATION_CODE))

        _message = "Beste gebruiker, hierbij de bevestigingscode die u moet ingeven bij het ophalen van uw fiets\n\nUw Code is: {}".format(_code)

        self.sendMessageToUser(chatID, _message)
        return _code

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

    def hasNewUpdates(self):
        """This function checks if there are any new updates available.
        It will try to fetch any new updates for 2 seconds, after that it returns either True of False

        :return: Boolean (True or False)
        """
        _newUpdate = self.bot.getUpdates(self.current_response+1, limit=1, timeout=2)
        if len(_newUpdate) > 0:
            return True
        return False

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

    def registerUpdateID(self, id):
        if id > self.current_response:
            self.current_response = id
