import tkinter
from Handlers import DatabaseHandler, telegramHandler
from ProjectData import Constants
from Validate import make_random_code

class UserValidator(object):
    """This is de UserValidator-class
    It can autonomously handle a validation.
    The UserValidator class requires an active DatabaseHandler

    """

    __hasEnteredValidPersonalCode = False
    __randomCode = ''
    __personalCode = ''
    __attempts = 0
    __success = False

    def getValue(self):
        """Returns the value of run succes

        :return: if the validation was unssuccesfull it wil  return false, else it will return the personalCode formt he validated user
        """
        if self.__success:
            return self.__personalCode
        else:
            return self.__success

    def handleButtonClick(self):
        """This function handles the button click in the validation Field

        :return: nothing
        """
        self.__attempts += 1
        if self.__attempts >= Constants.MAX_LOGIN_ATTEMPTS:
            self.foreceStop()

        elif self.__hasEnteredValidPersonalCode:
            self.validateExternalCode()

        else:
            self.validatePersonalCode()

    def validateExternalCode(self):
        """validates the externalcode (i.e.: the code that the application sends to the user)
        After validating is will destroy the mainloop

        :return: nothing
        """
        _input = self._entryPersonalCode.get()
        if _input == self.__randomCode:
            self.__success = True

        else:
            self.__success = False

        self.stop()

    def foreceStop(self):
        self.__success = False
        self.stop()

    def stop(self):
        self._screenRoot.destroy()

    def validatePersonalCode(self):
        """This function will start the validation process

        :return: nothing
        """
        # Todo: Database meegeven in de constructor
        # database object aanmaken

        #ophalen personal Code
        self.__personalCode = self._entryPersonalCode.get()

        # Ophalen telegram chat id
        telegramChatCode = self.__databaseHandler.getChatIDFromPersonalCode(self.__personalCode)

        print(telegramChatCode)

        if telegramChatCode:
            self.__hasEnteredValidPersonalCode = True

            _telegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)

            #Todo: Importeren Random Code genrator
            self.__randomCode = 'QWERTY' # Todo <----- Here!

            _telegramHandler.sendMessageToUser(telegramChatCode, self.__randomCode)

            _newMessage = 'Geef de ontvangen code a.u.b. in'
            self._labelMessage.configure(text=_newMessage)

        self._entryPersonalCode.delete(0, tkinter.END)


    def __init__(self, database):
        """
            Constructor
        """

        self.__databaseHandler = database

        self._screenRoot = tkinter.Tk()
        self._screenRoot.title('Fiets stallen')


        # Label toeveogen aan het popup scherm
        _labelText = 'Geef uw persoonlijke code'
        self._labelMessage = tkinter.Label(
            master=self._screenRoot,
            text=_labelText
        )
        self._labelMessage.grid(row=0)

        # invoer-balk toevoegen
        # hierin kan de gebruiker zijn eprsoonlijke code ingeven
        self._entryPersonalCode = tkinter.Entry(
            master=self._screenRoot
        )
        self._entryPersonalCode.grid(row=1)

        # Voeg een button toe aan het pop-up scherm
        # de gebruiker kan hier mee aangeven dat hij de code heeft ingevoerd
        _buttonConfirmCodeText = 'Gereed'

        self._buttonConfirmCode = tkinter.Button(
            master=self._screenRoot,
            text=_buttonConfirmCodeText,
            command=self.handleButtonClick
        )
        self._buttonConfirmCode.grid(row=2)

        self._screenRoot.mainloop()

