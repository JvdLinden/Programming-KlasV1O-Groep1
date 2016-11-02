from tkinter import *
def start_screen():
    root = Tk()

    message = Label(master=root, text='Welkom bij de fietsenstalling! \n'
                                  'Kies één van de volgende opties.')
    message.pack()

    reg_button = Button(master=root, text='Registeren').grid(row=1, column=0)
    stallen_button = Button(master=root, text='Stallen').grid(row=1, column= 1)
    ophalen_button = Button(master=root, text='Stallen').grid(row=1, column= 2)
    info_button = Button(master=root, text='Stallen').grid(row=1, column= 3)

    root.mainloop()
start_screen()
