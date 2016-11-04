import telepot
import string
import random
from ProjectData import constants


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
        # Attempt to send a message
        try:
            return self.bot.sendMessage(chat_id, message, parse_mode='Markdown')

        # Catch TelegramErrors (i.e. 'chat not found')
        except telepot.exception.TelegramError as error:
            return error

    def sendValidationCodeToUser(self, chatID):
        """This functions generates a validation code and sends it to the chat corresponding to the chatID.

        :param chatID: the chat ID related to the user we want to message
        :return: the code sent to the user
        """
        _code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(constants.LENGTH_PERSONAL_CODE))

        _message = "Beste gebruiker, hierbij de bevestigingscode die u moet ingeven.\n\nUw Code is: {}".format(_code)

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
        return len(_newUpdate) > 0

    def registerUpdateID(self, updateId):
        """registers an update's id t the telegramHandler.

        :param updateId: the id of the update that should be registered
        :return: nothing
        """
        if updateId > self.current_response:
            self.current_response = updateId

    def generateRegisterMessageFromKey(self, userKey):
        """Generate a message to display to the user.
        The message contains the bot's name and the registrration key

        :param userKey: ke to convert to registration key
        :return: (registrationkey), (displayString)
        """
        _finalString = 'Bedankt voor uw registratie!\n Om uw registratie succesvol af te ronden moet u geistreren bij onze telegrambot.\n'
        _finalString += 'Bot: {}\n'.format(constants.BOT_NAME)
        _code = constants.CODE_HEADER_REGISTER + userKey
        _finalString += 'Bericht: {}\n'.format(_code)

        return _code, _finalString
