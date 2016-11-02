import tkinter
from Handlers import DatabaseHandler, telegramHandler

class StoreBikePopUp(object):

    def retrievePersonalChatId(self):


    def validatePersonalCode(self):
        """This function will start the validation process

        :return: nothing
        """
        # Ophalen telegram chat id
        telegramChatCode = self.retrievePersonalChatId()

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
        ).grid(row=0)

        # invoer-balk toevoegen
        # hierin kan de gebruiker zijn eprsoonlijke code ingeven
        self._entryPersonalCode = tkinter.Entry(
            master=self._screenRoot
        ).grid(row=1)

        # Voeg een button toe aan het pop-up scherm
        # de gebruiker kan hier mee aangeven dat hij de code heeft ingevoerd
        _buttonConfirmCodeText = 'Gereed'

        self._buttonConfirmCode = tkinter.Button(
            master=self._screenRoot,
            text=_buttonConfirmCodeText,
            command=self.validatePersonalCode
        ).grid(row=2)

        self._screenRoot.mainloop()


# Todo : Delete onderstaande
objectje = StoreBikePopUp()
