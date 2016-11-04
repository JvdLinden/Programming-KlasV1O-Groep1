from userValidator import UserValidator
import tkinter
from tkinter import messagebox
from ProjectData import Constants


class Ophalen(object):
    """The Ophalen-object handles all the processen related to retrieving a bike

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
            _result = theCombinedHandler.retrieveBike(_user)

            _message = 'Uw fiets is opgehaald' if _result else 'Uw fiets is niet aanwezig!'

            # Create a window to show personal information
            self.root = tkinter.Tk()

            # Title for personal information window
            self.root.title('Ophalen')

            label = tkinter.Label(
                self.root,
                text=_message
            )
            label.grid(row=0)

            button = tkinter.Button(
                self.root,
                text=Constants.BACK,
                command=self.stop
            )
            button.grid(row=1)

            self.running = True
            while self.running:
                self.root.update_idletasks()
                self.root.update()
            self.root.destroy()
        else:
            messagebox.showinfo("Fout", "Uw inloggegevens worden niet herkend")




