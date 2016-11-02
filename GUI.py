from tkinter import *
from enum import Enum
import registration


entries = []
labels = ["Naam: ", "Straat: ", "Huisnummer: ", "Postcode: ", "Tel.nummer: "]
data = []


class Info(Enum):
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4


def sub_personal_code():
    # Default subscreen settings
    sub_window = Toplevel(master=registration_window)
    sub_window.title("Popup")

    # Widget creation
    code_label = Label(sub_window, text="Voer de ontvangen code in: ").grid(row=0, sticky=W)
    code_entry = Entry(sub_window,)
    code_entry.grid(row=0, column=1)
    submit_button = Button(sub_window, text="submit", command=check_code(code_entry.get(), sub_window)).grid(row=1, column=1)


def sub_incorrect_data(incorrect_entry):
    sub_window = Toplevel(master=registration_window)
    sub_window.title("Incorrecte invoer")

    incorrect_label = Label(sub_window, text="De invoer is incorrect. Voer uw %s in." % incorrect_entry)
    ok_button = Button(sub_window, text="OK", command=sub_window.destroy)
    incorrect_label.pack()
    ok_button.pack()


def check_code(input_code, code_window):  # checks Telegram sent code to see if it matches user input.
    if input_code == security_code:
        code_window.destroy
    else:
        pass


def check_entries(entries):
    # Data starts out as dict with entries
    name = entries['name'].get()  # All the entries are converted to the input strings
    street = entries['street'].get()
    house_number = entries['house_number'].get()
    postal_code = entries['postal_code'].get()
    phone_number = entries['phone_number'].get()

    if True:  # With our data being valid we start a pop-up to ask for a security code sent to your phone.
        global security_code
        security_code = registration.send_msg_to_nr(phone_number)
        sub_personal_code()
    else:
        sub_incorrect_data()


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
    phone_nr_entry.grid(row=4, column=1)

    user_dict = {'uid': registration.randomID(),
                 'name': name_entry,
                 'street': street_entry,
                 'house_number': house_nr_entry,
                 'postal_code': postal_code_entry,
                 'phone_number': phone_nr_entry}
    # When the submit button is clicked, entries are checked for validity.
    submit_button = Button(registration_window, text="submit", command=check_entries(user_dict)).grid(row=5, column=1, sticky=E)

    # Init registration_window
    registration_window.mainloop()
registration_window = -1
security_code = -1
registration_init()

