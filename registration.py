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


def subPersonalCode(confirmationCode, master):
    """
    A pop-up containing a personal code for the user which they have to text to Telegram.
    :param confirmationCode: The code in question
    :return:
    """
    # Default subscreen settings
    sub_window = Toplevel(master=master)
    sub_window.lift()
    sub_window.title("Popup")

    # Widget creation
    codeLabel = Label(sub_window, text="Voer de ontvangen code in: ").grid(row=0, sticky=W)
    codeEntry = Entry(sub_window,)
    codeEntry.grid(row=0, column=1)
    submitButton = Button(sub_window, text="submit")
    submitButton.grid(row=1, column=1)


def subIncorrectData(incorrect_entry, master):
    """
    A pop-up to indicate to the user the registration process can't continue because of incorrect data.
    :param incorrect_entry: The Dutch name of the entry in question containing incorrect data
    :return: none
    """
    subWindow = Toplevel(master=master)
    subWindow.title("Incorrecte invoer")
    subWindow.lift()

    incorrectLabel = Label(subWindow, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
    ok_button = Button(subWindow, text="OK", command=subWindow.destroy)
    incorrectLabel.pack()
    ok_button.pack()


# Todo - Add comments / documentation
def checkEntries(entries, master, database):
    """
        Method validates entries and throws a pop-up when something isn't noted properly.
    :param entries: Data starts out as dictionary containing entries
    :return: no return value.
    """
    # All the entries are converted to individual input strings.
    name = entries['name'].get()  # This his hardcoded because the data type can vary.
    street = entries['street'].get()
    houseNumber = entries['house_number'].get()
    postalCode = entries['postal_code'].get()
    phoneNumber = entries['phone_number'].get()
    # Here we start validating our data. Using this construction means we don't validate the rest of the data if,
    # for example, the first variable is invalid. Instead it immediately jumps to a pop-up stating which entry is wrong.
    if not Validate.string(name):
        subIncorrectData('naam', master)
    elif not Validate.string(street):
        subIncorrectData('straat', master)
    elif not Validate.huisNr(houseNumber):
        subIncorrectData('huisnummer', master)
    elif not Validate.postcode(postalCode):
        subIncorrectData('postcode', master)
    elif not Validate.telNr(phoneNumber):
        subIncorrectData('telefoonnummer', master)
    else:
        # With our data being valid we start a pop-up containing a security code to send to Telegram.
        subPersonalCode(createConfirmationCode(), master)

        # add to database


def addToDatabase(database, data):
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


def registrationInit(database):
    """
    The window for registration. It contains labels and entries for entering 5 variables, which are passed to a database
    :return: none
    """
    # Default settings:
    registrationWindow = Tk()
    registrationWindow.title("NS Fietsenstalling")

    # widget creation
    nameLabel = Label(registrationWindow, text='Naam: ').grid(row=0, sticky=W)
    nameEntry = Entry(registrationWindow)
    nameEntry.grid(row=0, column=1)

    streetLabel = Label(registrationWindow, text='Straat: ').grid(row=1, sticky=W)
    streetEntry = Entry(registrationWindow)
    streetEntry.grid(row=1, column=1)

    houseNrLabel = Label(registrationWindow, text='Huisnummer: ').grid(row=2, sticky=W)
    houseNrEntry = Entry(registrationWindow)
    houseNrEntry.grid(row=2, column=1)

    postalCodeLabel = Label(registrationWindow, text='Postcode: ').grid(row=3, sticky=W)
    postalCodeEntry = Entry(registrationWindow)
    postalCodeEntry.grid(row=3, column=1)

    phoneNrLabel = Label(registrationWindow, text='Tel.nummer: ').grid(row=4, sticky=W)
    phoneNrEntry = Entry(registrationWindow)
    phoneNrEntry.insert(END, '06-')
    phoneNrEntry.grid(row=4, column=1)

    user_dict = {'uid': randomID(),
                 'name': nameEntry,
                 'street': streetEntry,
                 'house_number': houseNrEntry,
                 'postal_code': postalCodeEntry,
                 'phone_number': phoneNrEntry}
    # When the submit button is clicked, entries are checked for validity.
    submitButton = Button(registrationWindow, text="submit",
                           command=lambda: checkEntries(user_dict, registrationWindow, database))
    submitButton.grid(row=5, column=1, sticky=E)

    # Init registration_window
    registrationWindow.mainloop()

    
def createConfirmationCode():
    """Creates a confirmation code to be used in Telegram verification.
    :return: the confirmation code.
    """
    return Validate.makeRandomCode(Constants.RANDOM_CONFIRMATION_CODE_LENGTH, Validate.CodeType.ALL)


# ToDo : Finish Comments / Documentation!
def randomID():
    """Creates an identification code to be printed on the sticker stuck to the bike.
    :return: the identification code.
    """
    return Validate.makeRandomCode(Constants.LENGTH_VALIDATION_CODE, Validate.CodeType.DIGITS)

