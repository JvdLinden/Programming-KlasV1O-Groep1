from Validate import *
from ProjectData import Constants


class Info(Enum):  # Class specifying in what order the information during registration is processed
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4


def registration_init():
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

    
def create_confirmation_code():
    """Creates a confirmation code to be used in Telegram verification.
    :return: the confirmation code.
    """
    return makeRandomCode(Constants.RANDOM_CONFIRMATION_CODE_LENGTH, CodeType.ALL)


# ToDo : Finish Comments / Documentation!
def randomID():
    """Creates an identification code to be printed on the sticker stuck to the bike.

    :return:
    """
    return makeRandomCode(Constants.RANDOM_ID_LENGTH, CodeType.DIGITS)

