from tkinter import *


def algemeneInfo():
    """
    Create a GUI for algemene informatie

    :return: Returns a GUI Screen
    """
    # Create a screen to ad information
    algemeneInfoWindow = Tk()

    # Assign title to the screen
    algemeneInfoWindow.title('Algemene informatie')

    # Message on top of the screen
    topMessage = Label(master=algemeneInfoWindow, text='NS Fietsenstalling').grid(row=0)

    # Add opening text to page
    openingMessage = Label(master=algemeneInfoWindow, text='In de NS fietsenstalling kunt U uw fiets nu nog makkelijker stallen. Namelijk met gebruik van telegram!\n'
                            'Bij uw eerste aanmelding ontvangt U een persoonlijke code. Met gebruik van deze code kunt u vervolgens '
                            'uw fiets stallen en ophalen.\n').grid(row=1)

    # Add registration info to page
    registrationInfoLabel = Label(master=algemeneInfoWindow, text='Registratie\n'
                                  'Om uw fiets te registreren gaat u terug naar het hoofdmenu en kiest u voor \'registreren\'.\n'
                                  'U word hier gevraagd om een aantal persoonlijke gegevens in te voeren. Vervolgens word er \n'
                                  'een persoonlijke code voor u aangemaakt. U dient deze te bevestigen door deze te versturen naar ons via Telegram.\n'
                                  'Hierna kunt U uw fiets stallen en ophalen met behulp van de ontvangen code.\n'
                                  'Onthoud uw persoonlijke code dus goed!\n').grid(row=2)

    # Add Openingstijden to page
    openingTimesMessage = Label(master=algemeneInfoWindow,
                                text='Openingstijden\n'
                                'De NS fietsenstalling is 24 uur per dag 7 dagen in de week open. U kunt uw fiets dus '
                                'altijd veilig stallen!').grid(row=3)

    # Button back to start screen
    backToStartButton = Button(master=algemeneInfoWindow, text='Terug naar start', command=lambda: close_window(algemeneInfoWindow)).grid(row=4)

    algemeneInfoWindow.mainloop()


def close_window(window):
    window.destroy()
