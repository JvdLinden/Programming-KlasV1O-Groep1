import validate
import tkinter
import time
from enum import Enum
from ProjectData import constants, messages
from tkinter import messagebox
from specialPopUp import SpecialPopUp


class Info(Enum):  # Class specifying in what order the information during registration is processed
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4


class RegistrationForm(object):

    def __init__(self, myCombinedHandler):
        """
        The window for registration. It contains labels and entries for entering 5 variables, which are passed to a database
        :return: none
        """
        self.myCombinedHandler = myCombinedHandler

        # Default settings:
        self.registrationWindow = tkinter.Tk()
        self.registrationWindow.title("NS Fietsenstalling")

        # widget creation
        self.nameLabel = tkinter.Label(self.registrationWindow, text='Naam: ')
        self.nameLabel.grid(row=0, sticky=tkinter.W)

        self.nameEntry = tkinter.Entry(self.registrationWindow)
        self.nameEntry.grid(row=0, column=1)

        self.streetLabel = tkinter.Label(self.registrationWindow, text='Straat: ')
        self.streetLabel.grid(row=1, sticky=tkinter.W)

        self.streetEntry = tkinter.Entry(self.registrationWindow)
        self.streetEntry.grid(row=1, column=1)

        self.houseNrLabel = tkinter.Label(self.registrationWindow, text='Huisnummer: ')
        self.houseNrLabel.grid(row=2, sticky=tkinter.W)

        self.houseNrEntry = tkinter.Entry(self.registrationWindow)
        self.houseNrEntry.grid(row=2, column=1)

        self.postalCodeLabel = tkinter.Label(self.registrationWindow, text='Postcode: ')
        self.postalCodeLabel.grid(row=3, sticky=tkinter.W)

        self.postalCodeEntry = tkinter.Entry(self.registrationWindow)
        self.postalCodeEntry.grid(row=3, column=1)

        self.phoneNrLabel = tkinter.Label(self.registrationWindow, text='Tel.nummer: ')
        self.phoneNrLabel.grid(row=4, sticky=tkinter.W)

        self.phoneNrEntry = tkinter.Entry(self.registrationWindow)

        self.phoneNrEntry.insert(tkinter.END, '06-')
        self.phoneNrEntry.grid(row=4, column=1)

        userDict = {'uid': self.randomID(),
                     'name': self.nameEntry,
                     'street': self.streetEntry,
                     'house_number': self.houseNrEntry,
                     'postal_code': self.postalCodeEntry,
                     'phone_number': self.phoneNrEntry}

        # When the submit button is clicked, entries are checked for validity.
        self.submitButton = tkinter.Button(
            self.registrationWindow,
            text=constants.SUBMIT,
            command=lambda: self.checkEntries(userDict)
        )
        self.submitButton.grid(row=5, column=1, sticky=tkinter.E)

    def start(self):
        # Init registration_window
        self.registrationWindow.mainloop()

    def stop(self):
        self.registrationWindow.destroy()

    def createConfirmationCode(self):
        """Creates a confirmation code to be used in Telegram verification.

        :return: the confirmation code.
        """
        return validate.makeRandomCode(constants.LENGTH_RANDOM_CONFIRMATION_CODE, validate.CodeType.ALL)

    # todo Dit invullen
    def createBikeCode(self):
        """

        :return:
        """
        return validate.makeRandomCode(constants.LENGTH_PERSONAL_CODE, validate.CodeType.ALL)

    def randomID(self):
        """Creates an identification code to be printed on the sticker stuck to the bike.

        :return: the identification code.
        """
        return validate.makeRandomCode(constants.LENGTH_PERSONAL_CODE, validate.CodeType.DIGITS)

    def subPersonalCode(self, registration_code):
        """
        A pop-up containing a personal code for the user which they have to text to Telegram.
        :param confirmationCode: The code in question
        :return:
        """

        SpecialPopUp(self.registrationWindow,
                     "Registreren",
                     "Stuur het volgende Telegram-bericht naar %s op Telegram." % constants.BOT_NAME,
                     "\n%s\n" % registration_code
                     )


    def subIncorrectData(self, incorrect_entry):
        """
        A pop-up to indicate to the user the registration process can't continue because of incorrect data.
        :param incorrect_entry: The Dutch name of the entry in question containing incorrect data
        :return: none
        """
        subWindow = tkinter.Toplevel(master=self.registrationWindow)
        subWindow.title("Incorrecte invoer")
        subWindow.lift()

        incorrectLabel = tkinter.Label(subWindow, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
        ok_button = tkinter.Button(subWindow, text=constants.BACK, command=subWindow.destroy)
        incorrectLabel.pack()
        ok_button.pack()

    def checkEntries(self, entries):
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
        if not validate.string(name):
            self.subIncorrectData('naam')
        elif not validate.string(street):
            self.subIncorrectData('straat')
        elif not validate.huisNr(houseNumber):
            self.subIncorrectData('huisnummer')
        elif not validate.postcode(postalCode):
            self.subIncorrectData('postcode')
        elif not validate.telNr(phoneNumber):
            self.subIncorrectData('telefoonnummer')
        else:
            # With our data being valid we start a pop-up containing a security code to send to Telegram.
            registrationCode = self.createConfirmationCode()

            self.subPersonalCode(registrationCode)

            # Format data for database
            userDict = {
                'name': name,
                'street': street,
                'house_nr': houseNumber,
                'postal_code': postalCode,
                'phone_nr': phoneNumber,
                'reg_key': registrationCode,
                'bike_key': self.createBikeCode()
            }
            self.myCombinedHandler.registerNewUser(userDict)

            # Loop to keep checking if reg key has been entered, when successful res gives chat ID
            _chatId = self.myCombinedHandler.getChatIdViaRegistrationKeyInLoggedUpdates(registrationCode)
            _count = 0
            while not _chatId:
                time.sleep(constants.REGISTRATION_WAIT)
                _count += 1
                if _count > constants.REGISTRATION_TIMEOUT:
                    break

                self.myCombinedHandler.handleUpdates()
                _chatId = self.myCombinedHandler.getChatIdViaRegistrationKeyInLoggedUpdates(registrationCode)


            if _chatId:
                self.myCombinedHandler.registerChatIdToUserViaRegKey(registrationCode, _chatId)


                SpecialPopUp(self.registrationWindow,
                             "Geregistreerd",
                             messages.GEREGISTREERD_POPUP,
                             userDict['bike_key']
                             )
                _message =  messages.GEREGISTREERD_TELEGRAM.format(userDict['bike_key'])

                self.myCombinedHandler.telegram.sendMessageToUser(_chatId, _message)
            else:
                messagebox.showinfo("TIME OUT", messages.REGISTRATIE_TIMEOUT)
            self.registrationWindow.destroy()
