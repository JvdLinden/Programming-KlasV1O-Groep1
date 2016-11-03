import Validate
from ProjectData import Constants
from tkinter import *
from enum import Enum

class Info(Enum):  # Class specifying in what order the information during registration is processed
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4


# Todo - Add comments / documentation
def sub_personal_code(confirmation_code, master):
    """
    A pop-up containing a personal code for the user which they have to text to Telegram.
    :param confirmation_code: The code in question
    :return:
    """
    # Default subscreen settings
    sub_window = Toplevel(master=master)
    sub_window.lift()
    sub_window.title("Popup")

    # Widget creation
    code_label = Label(sub_window, text="Voer de ontvangen code in: ").grid(row=0, sticky=W)
    code_entry = Entry(sub_window,)
    code_entry.grid(row=0, column=1)
    submit_button = Button(sub_window, text="submit")
    submit_button.grid(row=1, column=1)


# Todo - Add comments / documentation
def sub_incorrect_data(incorrect_entry, master):
    """
    A pop-up to indicate to the user the registration process can't continue because of incorrect data.
    :param incorrect_entry: The Dutch name of the entry in question containing incorrect data
    :return: none
    """
    sub_window = Toplevel(master=master)
    sub_window.title("Incorrecte invoer")
    sub_window.lift()

    incorrect_label = Label(sub_window, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
    ok_button = Button(sub_window, text="OK", command=sub_window.destroy)
    incorrect_label.pack()
    ok_button.pack()


# Todo - Add comments / documentation
def check_entries(entries, master, database):
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
        sub_incorrect_data('naam', master)
    elif not Validate.string(street):
        sub_incorrect_data('straat', master)
    elif not Validate.huisNr(house_number):
        sub_incorrect_data('huisnummer', master)
    elif not Validate.postcode(postal_code):
        sub_incorrect_data('postcode', master)
    elif not Validate.telNr(phone_number):
        sub_incorrect_data('telefoonnummer', master)
    else:
        # With our data being valid we start a pop-up containing a security code to send to Telegram.
        sub_personal_code(create_confirmation_code(), master)

        # add to database


def add_to_database(database, data):
    """

    :param database: instance of a database handler
    :param data: dictionary containing relevant data for registration
    :return: whether the method succeeded or not
    """
    '''
    This block of code will be the database transition
        {   'sticker': randomID(),
            'name': data['name'],
            'street': data['street'],
            'house_number': data['house_number'],
            'postal_code': data['postal_code'],
            'phone_number': data['phone_number']}
    '''


def registration_init(database):
    """
    The window for registration. It contains labels and entries for entering 5 variables, which are passed to a database
    :return: none
    """
    # Default settings:
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

    user_dict = {'uid': randomID(),
                 'name': name_entry,
                 'street': street_entry,
                 'house_number': house_nr_entry,
                 'postal_code': postal_code_entry,
                 'phone_number': phone_nr_entry}
    # When the submit button is clicked, entries are checked for validity.
    submit_button = Button(registration_window, text="submit", command=lambda: check_entries(user_dict, registration_window, database)).grid(row=5, column=1, sticky=E)

    # Init registration_window
    registration_window.mainloop()

    
def create_confirmation_code():
    """Creates a confirmation code to be used in Telegram verification.
    :return: the confirmation code.
    """
    return Validate.makeRandomCode(Constants.RANDOM_CONFIRMATION_CODE_LENGTH, Validate.CodeType.ALL)


# ToDo : Finish Comments / Documentation!
def randomID():
    """Creates an identification code to be printed on the sticker stuck to the bike.

    :return:
    """
    return Validate.makeRandomCode(Constants.LENGTH_VALIDATION_CODE, Validate.CodeType.DIGITS)

