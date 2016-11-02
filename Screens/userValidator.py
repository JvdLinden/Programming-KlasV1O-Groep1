import tkinter
from tkinter import messagebox
from Handlers import DatabaseHandler, telegramHandler
from ProjectData import Constants

class UserValidator(object):

    __hasEnteredValidPersonalCode = False
    __randomCode = ''
    __personalCode = ''
    __success = False

    def getValue(self):
        return self.__success

    def handleButtonClick(self):
        if self.__hasEnteredValidPersonalCode:
            self.validateExternalCode()
        else:
            self.validatePersonalCode()

    def validateExternalCode(self):
        _input = self._entryPersonalCode.get()
        if _input == self.__randomCode:
            self._screenRoot.destroy()
            self.__success = True

        else:
            # Reset the Button handling
            self.__hasEnteredValidPersonalCode = False

    def validatePersonalCode(self):
        """This function will start the validation process

        :return: nothing
        """
        # Todo: Database meegeven in de constructor
        # database object aanmaken
        _databaseHandler = DatabaseHandler.DatabaseHandler(Constants.DATABASE_MASK)

        #ophalen personal Code
        self.__personalCode = self._entryPersonalCode.get()

        # Ophalen telegram chat id
        telegramChatCode = _databaseHandler.getChatIDFromPersonalCode(self.__personalCode)

        # verwijder database instantie
        del _databaseHandler

        self.__hasEnteredValidPersonalCode = True

        _telegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)

        #Todo: Importeren Random Code genrator
        self.__randomCode = 'QWERTY' # Todo <----- Here!

        _telegramHandler.sendMessageToUser(telegramChatCode, self.__randomCode)

        _newMessage = 'Geef de ontvangen code a.u.b. in'
        self._labelMessage.configure(text=_newMessage)
        self._entryPersonalCode.delete(0, tkinter.END)


    def __init__(self):
        """
            Constructor
        """

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

# Todo : onderstaande mag weg, maar dient als voorbeeld
# Create a validator object
objectje = UserValidator()

# when the validator object is done running, retrieve the value.
newValue = objectje.getValue()

# print Value
print(newValue)
