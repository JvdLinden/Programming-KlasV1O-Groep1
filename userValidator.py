import tkinter
from Handlers import telegramHandler
from ProjectData import Constants


class UserValidator(object):
    """This is de UserValidator-class
    It can autonomously handle a validation.
    The UserValidator class requires an active DatabaseHandler

    """

    # This variable tracks whether the user entered a valid personal code
    __hasEnteredValidPersonalCode = False

    # The final result of the interaction, will be True after a successful validation
    __success = False

    # The validation key
    __randomCode = ''

    # The personal user code
    __personalCode = ''

    # Amount of validation attempts
    __attempts = 0

    def getValue(self):
        """Returns the value of run success

        :return: if successful: the user_id, else it will return false
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
        """This will stop the mainloop and thus kill the windows opened by this class.
        Also it will set the result to 'False', meaning the validation has failed.

        :return: nothing
        """
        self.__success = False
        self.stop()

    def stop(self):
        """Stops the mainloop and kills all windows

        :return:
        """
        self.running = False

    def validatePersonalCode(self):
        """This function will start the validation process

        :return: nothing
        """

        #ophalen personal Code
        self.__personalCode = self._entryPersonalCode.get()

        # Ophalen telegram chat id
        telegramChatCode = self.__combinedHandler.database.getChatIDFromPersonalCode(self.__personalCode)

        if telegramChatCode:
            self.__hasEnteredValidPersonalCode = True

            self.__randomCode = self.__combinedHandler.telegram.sendValidationCodeToUser(telegramChatCode)

            _newMessage = 'Geef de ontvangen code a.u.b. in'
            self._labelMessage.configure(text=_newMessage)

        self._entryPersonalCode.delete(0, tkinter.END)

    def __init__(self, combinedHandler, master):
        """
            Constructor
        """

        self.__combinedHandler = combinedHandler

        self._screenRoot = tkinter.Toplevel(master)
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

        self._buttonConfirmCode = tkinter.Button(
            master=self._screenRoot,
            text=Constants.SUBMIT,
            command=self.handleButtonClick
        )
        self._buttonConfirmCode.grid(row=2)

        self.running = True
        while self.running:
            self._screenRoot.update_idletasks()
            self._screenRoot.update()
        self._screenRoot.destroy()

