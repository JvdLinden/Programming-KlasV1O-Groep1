from Algemene_info import *
import registration

def startScreen():
    """Create the GUI for the main screen.

    :return: returns a GUI screen
    """
    # Create a root screen for the GUI to add items into
    root = Tk()

    # Assign a title to the screen
    root.title('Fietsenstalling beheer')

    # Welcome message
    message = Label(master=root, text='Welkom bij de fietsenstalling! \n'
                                  'Kies één van de volgende opties.').grid(row=0, column=0)

    # Adding 'Registreren'-button
    buttonRegister = Button(master =root, text='Registeren', command=registration.registration_init)
    buttonRegister.grid(row=1, column=0)

    # Adding 'Stallen'-button
    # ToDo : Add command to button
    buttonStore = Button(master=root, text='Stallen').grid(row=2, column=0)

    # Adding 'Ophalen'-button
    # ToDo : Add command to button
    buttonRetrieve = Button(master=root, text='Ophalen').grid(row=3, column=0)

    # Adding 'Algemene Informatie'-button
    buttonInfo = Button(master=root, text='Algemene Informatie', command=algemene_info).grid(row=4, column=0)

    # Adding 'Persoonlijke Informatie'-button
    # ToDo : Add command to button
    buttonPersonalInfo = Button(master=root, text='Persoonlijke Informatie').grid(row=5, column=0)

    return root

screen = startScreen()
screen.mainloop()




