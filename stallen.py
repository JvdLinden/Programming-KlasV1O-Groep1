from userValidator import UserValidator
import tkinter


class Stallen(object):

    def stop(self):
        self.running = False

    def __init__(self, theCombinedHandler, master):
        # validate user
        usval = UserValidator(theCombinedHandler, master)
        _user = usval.getValue()
        del usval

        theCombinedHandler.storeBike(_user)

        # Create a window to show personal information
        self.root = tkinter.Tk()

        # Title for personal information window
        self.root.title('Stallen')


        label = tkinter.Label(self.root, text='Uw Fiets is gestald!')
        label.grid(row=0)

        button = tkinter.Button(self.root, text='Oke', command=self.stop)
        button.grid(row=1)

        self.running = True
        while self.running:
            self.root.update_idletasks()
            self.root.update()
        self.root.destroy()




