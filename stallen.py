from userValidator import UserValidator
import tkinter
from tkinter import messagebox

class Stallen(object):

    def stop(self):
        self.running = False

    def __init__(self, theCombinedHandler, master):
        # validate user
        usval = UserValidator(theCombinedHandler, master)
        _user = usval.getValue()
        del usval
        if _user:
            _stalResult = theCombinedHandler.storeBike(_user)

            # Create a window to show personal information
            self.root = tkinter.Tk()
            self.root.geometry('222x111')
            # Title for personal information window
            self.root.title('Stallen')

            label = tkinter.Label(self.root, text=_stalResult)
            label.grid(row=0)

            button = tkinter.Button(self.root, text='Oke', command=self.stop)
            button.grid(row=1)

            self.running = True
            while self.running:
                self.root.update_idletasks()
                self.root.update()
            self.root.destroy()
        else:
            messagebox.showinfo("Fout", "Uw inloggegevens worden niet herkend")





