import tkinter


class SpecialPopUp(object):
    """This class defines a special pop-up that won't mess with the mainloop.

    """
    def stop(self):
        """Stops the loop, resulting into closing the object

        :return: nothing
        """
        self.running = False

    def __init__(self, master, title, text, selectableText):
        """Creates a SpecialPopUp - object.

        :param master: the screen from which the pop-up is called
        :param title: the title for the pop-up screen
        :param text: the body of the pop-up
        :param selectableText: the ext on the pop-up that should be selectable by the user
        """
        self.root = tkinter.Toplevel(master)
        self.root.title(title)
        lab = tkinter.Label(master=self.root, text=text)
        lab.grid(row=0)
        ent = tkinter.Entry(self.root)
        ent.delete(0, tkinter.END)
        ent.insert(0, str(selectableText))
        ent['state'] = 'readonly'
        ent.grid(row=1)
        button = tkinter.Button(master=self.root, text='Oke', command=self.stop)
        button.grid(row=2)

        self.running = True
        while self.running:
            self.root.update_idletasks()
            self.root.update()
        self.root.destroy()

