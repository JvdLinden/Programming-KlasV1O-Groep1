import AlgemeneInfo
import tkinter
from Handlers import databaseHandler, telegramHandler
from ProjectData import Constants
import registration

class GUI(object):

    def __init__(self, database, telegram):
        """Create the GUI for the main screen.

        :return: an GUI object
        """
        self.database = database
        self.telegram = telegram

        # Create a root screen for the GUI to add items into
        self.root = tkinter.Tk()

        # Assign a title to the screen
        self.root.title('Fietsenstalling beheer')

        # Welcome message
        self.message = tkinter.Label(
            master=self.root,
            text='Welkom bij de fietsenstalling! \nKies één van de volgende opties.'
        )
        self.message.grid(row=0, column=0)

        # Adding 'Registreren'-button
        self.buttonRegister = tkinter.Button(
            master=self.root,
            text='Registeren',
            command=lambda: registration.RegistrationForm(database)
        )
        self.buttonRegister.grid(row=1, column=0)

        # Adding 'Stallen'-button
        # ToDo : Add command to button
        self.buttonStore = tkinter.Button(
            master=self.root,
            text='Stallen'
        )
        self.buttonStore.grid(row=2, column=0)

        # Adding 'Ophalen'-button
        # ToDo : Add command to button
        self.buttonRetrieve = tkinter.Button(
            master=self.root,
            text='Ophalen'
        )
        self.buttonRetrieve.grid(row=3, column=0)

        # Adding 'Algemene Informatie'-button
        self.buttonInfo = tkinter.Button(
            master=self.root,
            text='Algemene Informatie',
            command=AlgemeneInfo.algemeneInfo
        )
        self.buttonInfo.grid(row=4, column=0)

        # Adding 'Persoonlijke Informatie'-button
        # ToDo : Add command to button
        self.buttonPersonalInfo = tkinter.Button(
            master=self.root,
            text='Persoonlijke Informatie'
        )
        self.buttonPersonalInfo.grid(row=5, column=0)

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()


myDatabaseHandler = databaseHandler.DatabaseHandler(Constants.DATABASE)
myTelegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)

screen = GUI(database=databaseHandler, telegram=myTelegramHandler)
screen.start()




