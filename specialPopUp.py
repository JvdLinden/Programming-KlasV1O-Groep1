import tkinter


class SpecialPopUp(object):

    def stop(self):
        self.running = False

    def __init__(self, master, title, text, selectableText):
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

