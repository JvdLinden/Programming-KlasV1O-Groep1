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
            text='\nWelkom bij de fietsenstalling! \nKies één van de volgende opties.\n',
            width=50,
            bg='yellow'
        )
        self.message.grid(row=0)

        # Adding 'Registreren'-button
        self.buttonRegister = tkinter.Button(
            master=self.root,
            text='Registeren',
            command=lambda: registration.RegistrationForm(database),
            width=15,
            pady=8
        )
        self.buttonRegister.grid(row=1)

        # Adding 'Stallen'-button
        # ToDo : Add command to button
        self.buttonStore = tkinter.Button(
            master=self.root,
            text='Stallen',
            width=15,
            pady=8
        )
        self.buttonStore.grid(row=2)

        # Adding 'Ophalen'-button
        # ToDo : Add command to button
        self.buttonRetrieve = tkinter.Button(
            master=self.root,
            text='Ophalen',
            width=15,
            pady=8
        )
        self.buttonRetrieve.grid(row=3)

        # Adding 'Algemene Informatie'-button
        self.buttonInfo = tkinter.Button(
            master=self.root,
            text='Algemene Informatie',
            command=AlgemeneInfo.algemeneInfo,
            width=15,
            pady=8
        )
        self.buttonInfo.grid(row=4)

        # Adding 'Persoonlijke Informatie'-button
        # ToDo : Add command to button
        self.buttonPersonalInfo = tkinter.Button(
            master=self.root,
            text='Persoonlijke Informatie',
            width=15,
            pady=8
        )
        self.buttonPersonalInfo.grid(row=5)

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()


myDatabaseHandler = databaseHandler.DatabaseHandler(Constants.DATABASE)
myTelegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)

screen = GUI(database=databaseHandler, telegram=myTelegramHandler)
screen.start()




