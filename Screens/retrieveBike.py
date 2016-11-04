import tkinter
from Handlers import DatabaseHandler, telegramHandler
from ProjectData import constants
from userValidator import UserValidator

class RetrieveBikePopUp(object):

# Vragen om invoer PersonalCode
# Pop-Up scherm met input mogelijkheid en vraag persoonlijke code

    def __init__(self):
        """
            Constructor
        """
        self._screenRoot = tkinter.Tk()
        self._screenRoot.title('Fiets ophalen')

        # label toevoegen aan popup
        _labelText = 'Geef uw persoonlijke code'
        self._labelMessage = tkinter.Label(
            master=self._screenRoot,
            text=_labelText
        )
        self._labelMessage.grid(row=0)

        # invoegvlak voor persoonlijke code toevoegen
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
            #command=self.handleButtonClick
        )
        self._buttonConfirmCode.grid(row=2)

        print('check')
        x = UserValidator()
        print('check')
        del x
        print('DELETED X')

        self._screenRoot.mainloop()


# Bevestigingscode versturen naar TelegramCode die bij PersonalCode hoort
# vanuit telegramBot
# Vragen om bevestigingscode
# Fiets vrijgeven


myObject = UserValidator()
myObject2 = myObject.getValue()
print(myObject2)
