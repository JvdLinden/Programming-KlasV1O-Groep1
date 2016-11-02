from tkinter import *

#Function for starting Home screen
def start_screen():
    root = Tk()
    root.title('Fietsenstalling beheer')

    #Welcome message
    message = Label(master=root, text='Welkom bij de fietsenstalling! \n'
                                  'Kies één van de volgende opties.').grid(row=0, column=0)

    #Buttons to differente functions
    #Commands not made yet
    reg_button = Button(master=root, text='Registeren').grid(row=1, column=0)
    stallen_button = Button(master=root, text='Stallen').grid(row=2, column=0)
    ophalen_button = Button(master=root, text='Ophalen').grid(row=3, column=0)
    alg_info_button = Button(master=root, text='Algemene Informatie').grid(row=4, column=0)
    pers_info_button = Button(master=root, text='Persoonlijke Informatie').grid(row=5, column=0)

    root.mainloop()

start_screen()
