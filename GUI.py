from tkinter import *
from enum import Enum
import registration
import Validate


labels = ["Naam: ", "Straat: ", "Huisnummer: ", "Postcode: ", "Tel.nummer: "]
# CONSTANTS
TELEGRAM_BOT_NAME = '@Fietsenstalling_Beheer_Bot'


class Info(Enum):
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4


def sub_personal_code(confirmation_code):
    # Default subscreen settings
    sub_window = Toplevel(master=registration_window)
    sub_window.lift()
    sub_window.title("Popup")

    # Widget creation
    code_label = Label(sub_window, text="Voer de ontvangen code in: ").grid(row=0, sticky=W)
    code_entry = Entry(sub_window,)
    code_entry.grid(row=0, column=1)
    submit_button = Button(sub_window, text="submit")
    submit_button.grid(row=1, column=1)


def sub_incorrect_data(incorrect_entry):
    sub_window = Toplevel(master=registration_window)
    sub_window.title("Incorrecte invoer")
    sub_window.lift()

    incorrect_label = Label(sub_window, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
    ok_button = Button(sub_window, text="OK", command=sub_window.destroy)
    incorrect_label.pack()
    ok_button.pack()


def check_entries(entries):
    # Method validates entries and throws a pop-up when something isn't noted properly.
    # Data starts out as dict with entries
    name = entries['name'].get()  # All the entries are converted to the input strings
    street = entries['street'].get()
    house_number = entries['house_number'].get()
    postal_code = entries['postal_code'].get()
    phone_number = entries['phone_number'].get()
    if not validate.string(name):
        sub_incorrect_data('naam')
    elif not validate.string(street):
        sub_incorrect_data('straat')
    elif not validate.huis_nr(house_number):
        sub_incorrect_data('huisnummer')
    elif not validate.postcode(postal_code):
        sub_incorrect_data('postcode')
    elif not validate.tel_nr(phone_number):
        sub_incorrect_data('telefoonnummer')
    else:
      # With our data being valid we start a pop-up containing a security code to send to Telegram.
        sub_personal_code(registration.send_msg_to_nr(phone_number))


def registration_init():
    # Default settings:
    global registration_window
    registration_window = Tk()
    registration_window.title("NS Fietsenstalling")

    # widget creation
    name_label = Label(registration_window, text='Naam: ').grid(row=0, sticky=W)
    name_entry = Entry(registration_window)
    name_entry.grid(row=0, column=1)

    street_label = Label(registration_window, text='Straat: ').grid(row=1, sticky=W)
    street_entry = Entry(registration_window)
    street_entry.grid(row=1, column=1)

    house_nr_label = Label(registration_window, text='Huisnummer: ').grid(row=2, sticky=W)
    house_nr_entry = Entry(registration_window)
    house_nr_entry.grid(row=2, column=1)

    postal_code_label = Label(registration_window, text='Postcode: ').grid(row=3, sticky=W)
    postal_code_entry = Entry(registration_window)
    postal_code_entry.grid(row=3, column=1)

    phone_nr_label = Label(registration_window, text='Tel.nummer: ').grid(row=4, sticky=W)
    phone_nr_entry = Entry(registration_window)
    phone_nr_entry.insert(END, '06-')
    phone_nr_entry.grid(row=4, column=1)

    user_dict = {'uid': registration.randomID(),
                 'name': name_entry,
                 'street': street_entry,
                 'house_number': house_nr_entry,
                 'postal_code': postal_code_entry,
                 'phone_number': phone_nr_entry}
    # When the submit button is clicked, entries are checked for validity.
    submit_button = Button(registration_window, text="submit", command=lambda: check_entries(user_dict)).grid(row=5, column=1, sticky=E)

    # Init registration_window
    registration_window.mainloop()


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
    buttonRegister = Button(master =root, text='Registeren', command=registration_init).grid(row=1, column=0)

    # Adding 'Stallen'-button
    # ToDo : Add command to button
    buttonStore = Button(master=root, text='Stallen').grid(row=2, column=0)

    # Adding 'Ophalen'-button
    # ToDo : Add command to button
    buttonRetrieve = Button(master=root, text='Ophalen').grid(row=3, column=0)

    # Adding 'Algemene Informatie'-button
    # ToDo : Add command to button
    buttonInfo = Button(master=root, text='Algemene Informatie').grid(row=4, column=0)

    # Adding 'Persoonlijke Informatie'-button
    # ToDo : Add command to button
    buttonPersonalInfo = Button(master=root, text='Persoonlijke Informatie').grid(row=5, column=0)

    return root

screen = startScreen()
screen.mainloop()




