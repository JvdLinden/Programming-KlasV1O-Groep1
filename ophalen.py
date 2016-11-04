from userValidator import UserValidator
import tkinter
from tkinter import messagebox
from ProjectData import Constants

class Ophalen(object):

    def stop(self):
        self.running = False

    def __init__(self, theCombinedHandler, master):
        # validate user
        usval = UserValidator(theCombinedHandler, master)
        _user = usval.getValue()
        del usval
        if _user:
            _result = theCombinedHandler.retrieveBike(_user)

            _message = 'Uw fiets is opgehaald' if _result else 'Uw fiets is niet aanwezig!'

            # Create a window to show personal information
            self.root = tkinter.Tk()

            # Title for personal information window
            self.root.title('Ophalen')

            label = tkinter.Label(self.root, text=_message)
            label.grid(row=0)

            button = tkinter.Button(self.root, text=Constants.BACK, command=self.stop)
            button.grid(row=1)

            self.running = True
            while self.running:
                self.root.update_idletasks()
                self.root.update()
            self.root.destroy()
        else:
             messagebox.showinfo("Fout", "Uw inloggegevens worden niet herkend")




