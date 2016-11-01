from tkinter import *


def sub_personal_code():
    #Default subscreen settings
    sub_window = Toplevel(master=registration_window)
    sub_window.title('Popup')

    #Widget creation
    code_label = Label(sub_window, text='Voer de ontvangen code in: ').grid(row=0, sticky=W)
    code_entry = Entry(sub_window,).grid(row=0, column=1)

    submit_button = Button(sub_window, text='submit').grid(row=1, column=1)


def main():
    # Default settings:
    global registration_window
    registration_window = Tk()
    registration_window.title('NS Fietsenstalling')

    # widget creation
    name_label = Label(registration_window, text='Naam: ').grid(row=0, sticky=W)
    name_entry = Entry(registration_window).grid(row=0, column=1)

    street_label = Label(registration_window, text='Straat: ').grid(row=1, sticky=W)
    street_entry = Entry(registration_window).grid(row=1, column=1)

    house_nr_label = Label(registration_window, text='Huisnummer: ').grid(row=2, sticky=W)
    house_nr_entry = Entry(registration_window).grid(row=2, column=1)

    postal_code_label = Label(registration_window, text='Postcode: ').grid(row=3, sticky=W)
    postal_code_entry = Entry(registration_window).grid(row=3, column=1)

    phone_nr_label = Label(registration_window, text='Tel.nummer: ').grid(row=4, sticky=W)
    phone_nr_entry = Entry(registration_window).grid(row=4, column=1)

    submit_button = Button(registration_window, text='submit', command=sub_personal_code).grid(row=6, column=1)

    # Init registration_window
    registration_window.mainloop()

main()

