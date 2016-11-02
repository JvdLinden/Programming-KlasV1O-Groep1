import tkinter
from Handlers import DatabaseHandler, telegramHandler
from ProjectData import Constants

class StoreBikePopUp(object):

    def handleButtonClick(self):
        self.validatePersonalCode()

    def validatePersonalCode(self):
        """This function will start the validation process

        :return: nothing
        """
        # Todo: Database meegeven in de constructor
        #database object aanmaken
        _databaseHandler = DatabaseHandler.DatabaseHandler(Constants.DATABASE_MASK)

        # Ophalen telegram chat id
        telegramChatCode = _databaseHandler.getChatIDFromPersonalCode(self._entryPersonalCode.get())

        #verwijder database instantie
        del _databaseHandler

        _telegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)

        #Todo: Importeren Random Code genrator
        _RANDOM_CODE = 'QWERTY'

        _telegramHandler.sendMessageToUser(telegramChatCode, _RANDOM_CODE)


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


# Todo : Delete onderstaande
objectje = StoreBikePopUp()
