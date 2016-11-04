import tkinter
from tkinter import messagebox

from ProjectData import constants
from Validation.userValidator import UserValidator


class Stallen(object):
    """The Stallen-object handles all the processen related to retrieving a bike

    """

    def stop(self):
        """Stops the loop, resulting into closing the object

        :return: nothing
        """
        self.running = False

    def __init__(self, theCombinedHandler, master):
        """Creates an Ophalen-object

        :param theCombinedHandler: the combinedHandler object that is being used in the application
        :param master: the parent of this screen
        """
        # validate user
        theUserValidator = UserValidator(theCombinedHandler, master)
        _user = theUserValidator.getValue()
        del theUserValidator
        if _user:
            _stalResult = theCombinedHandler.storeBike(_user)

            # Create a window to show personal information
            self.root = tkinter.Tk()
            self.root.geometry('222x111')
            # Title for personal information window
            self.root.title('Stallen')

            label = tkinter.Label(self.root, text=_stalResult)
            label.grid(row=0)

            button = tkinter.Button(self.root, text=constants.BACK, command=self.stop)
            button.grid(row=1)

            self.running = True
            while self.running:
                self.root.update_idletasks()
                self.root.update()
            self.root.destroy()
        else:
            messagebox.showinfo("Fout", "Uw inloggegevens worden niet herkend")






