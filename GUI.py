from tkinter import *
from userValidator import UserValidator
from Algemene_info import *
import registration
import Validate


# Array containing labels for registration
labels = ["Naam: ", "Straat: ", "Huisnummer: ", "Postcode: ", "Tel.nummer: "]
# CONSTANTS
TELEGRAM_BOT_NAME = '@Fietsenstalling_Beheer_Bot'


# Todo - Add comments / documentation
def sub_personal_code(confirmation_code):
    """
    A pop-up containing a personal code for the user which they have to text to Telegram.
    :param confirmation_code: The code in question
    :return:
    """
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


# Todo - Add comments / documentation
def sub_incorrect_data(incorrect_entry):
    """
    A pop-up to indicate to the user the registration process can't continue because of incorrect data.
    :param incorrect_entry: The Dutch name of the entry in question containing incorrect data
    :return: none
    """
    sub_window = Toplevel(master=registration_window)
    sub_window.title("Incorrecte invoer")
    sub_window.lift()

    incorrect_label = Label(sub_window, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
    ok_button = Button(sub_window, text="OK", command=sub_window.destroy)
    incorrect_label.pack()
    ok_button.pack()


# Todo - Add comments / documentation
def check_entries(entries):
    """
        Method validates entries and throws a pop-up when something isn't noted properly.
    :param entries: Data starts out as dictionary containing entries
    :return: no return value.
    """
    # All the entries are converted to individual input strings.
    name = entries['name'].get()  # This his hardcoded because the data type can vary.
    street = entries['street'].get()
    house_number = entries['house_number'].get()
    postal_code = entries['postal_code'].get()
    phone_number = entries['phone_number'].get()
    # Here we start validating our data. Using this construction means we don't validate the rest of the data if,
    # for example, the first variable is invalid. Instead it immediately jumps to a pop-up stating which entry is wrong.
    if not Validate.string(name):
        sub_incorrect_data('naam')
    elif not Validate.string(street):
        sub_incorrect_data('straat')
    elif not Validate.huisNr(house_number):
        sub_incorrect_data('huisnummer')
    elif not Validate.postcode(postal_code):
        sub_incorrect_data('postcode')
    elif not Validate.telNr(phone_number):
        sub_incorrect_data('telefoonnummer')
    else:
      # With our data being valid we start a pop-up containing a security code to send to Telegram.
        sub_personal_code(registration.create_confirmation_code())
        add_to_database()


def add_to_database(database, data):
    """

    :param database: instance of a database handler
    :param data: dictionary containing relevant data for registration
    :return: whether the method succeeded or not
    """
    '''
    This block of code will be the database transition
        {'sticker': randomID(),
            'name': data['name'],
            'street': data['street'],
            'house_number': data['house_number'],
            'postal_code': data['postal_code'],
            'phone_number': data['phone_number']}
    '''
    return False


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
    buttonInfo = Button(master=root, text='Algemene Informatie', command=algemene_info).grid(row=4, column=0)

    # Adding 'Persoonlijke Informatie'-button
    # ToDo : Add command to button
    buttonPersonalInfo = Button(master=root, text='Persoonlijke Informatie').grid(row=5, column=0)

    return root

screen = startScreen()
screen.mainloop()




