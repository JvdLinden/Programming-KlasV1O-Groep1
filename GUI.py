import AlgemeneInfo
import tkinter
from Handlers import combinedHandler
from ProjectData import Constants
import registration
import personal_info
import stallen
import ophalen


class GUI(object):

    def __init__(self, myCombinedHandler):
        """Create the GUI for the main screen.

        :return: an GUI object
        """
        self.myCombinedHandler = myCombinedHandler

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
            command=lambda: registration.RegistrationForm(myCombinedHandler),
            width=17,
            pady=8
        )
        self.buttonRegister.grid(row=1)

        # Adding 'Stallen'-button
        self.buttonStore = tkinter.Button(
            master=self.root,
            text='Stallen',
            command = lambda: stallen.Stallen(self.myCombinedHandler, self.root),
            width=17,
            pady=8
        )
        self.buttonStore.grid(row=2)

        # Adding 'Ophalen'-button
        # ToDo : Add command to button
        self.buttonRetrieve = tkinter.Button(
            master=self.root,
            text='Ophalen',
            command = lambda: ophalen.Ophalen(self.myCombinedHandler, self.root),
            width=17,
            pady=8
        )
        self.buttonRetrieve.grid(row=3)

        # Adding 'Algemene Informatie'-button
        self.buttonInfo = tkinter.Button(
            master=self.root,
            text='Algemene Informatie',
            command=AlgemeneInfo.algemeneInfo,
            width=17,
            pady=8
        )
        self.buttonInfo.grid(row=4)

        # Adding 'Persoonlijke Informatie'-button
        # ToDo : Add command to button
        self.buttonPersonalInfo = tkinter.Button(
            master=self.root,
            text='Persoonlijke Informatie',
            width=17,
            pady=8,
            command= personal_info.personal_info_screen
        )
        self.buttonPersonalInfo.grid(row=5)

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()

ch = combinedHandler.CombinedHandler(Constants.DATABASE_SHARED, Constants.BOT_TOKEN)
screen = GUI(ch)
screen.start()




