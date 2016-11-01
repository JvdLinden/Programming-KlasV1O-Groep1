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


def check_entries():
    global data
    for entry in entries:
        data.append(entry.get())  # All the data is gathered into the entry array
    res = registration.is_valid(data)  # res[0] being true means the entries are valid.
    # res[1] contains which entry is invalid should this not be the case.
    if res[0]:  # With our data being valid we start a pop-up to ask for a security code sent to your phone.
        global security_code
        security_code = registration.send_msg_to_nr(entries[Info.PHONE_NR.value])
        sub_personal_code()
    else:
        sub_incorrect_data(res[1])


def registration_init():
    # Default settings:
    global registration_window
    registration_window = Tk()
    registration_window.title("NS Fietsenstalling")

    # widget creation
    for i, label in enumerate(labels):  # labels is a string array here,

        label = Label(registration_window, text=label)
        label.grid(row=i, sticky=W)
        labels[i] = label  # but becomes a Label array here.
        textbox = Entry(registration_window)
        textbox.grid(row=i, column=1)
        entries.append(textbox)  # entries is created as an Entry array.

    # When the submit button is clicked, entries are checked for validity.
    submit_button = Button(registration_window, text="submit", command=check_entries).grid(row=5, column=1, sticky=E)

    # Init registration_window
    registration_window.mainloop()
registration_window = -1
security_code = -1
registration_init()

