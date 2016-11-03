from tkinter import *

    # "SELECT * FROM users WHERE personal_code = {}".format(personalcode)

def personal_info_start():
    """
    Create a GUI for Personal informatie

    :return: Returns a GUI Screen
    """

    # Create screen for personal logon
    personal_info_window = Tk()

    # Screen Title
    personal_info_window.title("Persoonlijke informatie")

    # Name label on top of screen
    name_label = Label(master=personal_info_window, text='Persoonlijke ID: ').grid(row=0)

    # Entry field for personal Code
    personal_id = Entry(master=personal_info_window).grid(row=1)

    # Submit button to submit personal code
    # ToDo : Add command to button
    submit_button = Button(master=personal_info_window, text='submit').grid(row=2)

    # Name Label for recieved code
    name_Label2 = Label(master=personal_info_window, text='Ontvangen code: ').grid(row=3)

    # Entry field for recieved code
    personal_code = Entry(master=personal_info_window).grid(row=4)

    # Submit button to submit recieved code
    # ToDo : Add command to button
    submit_button = Button(master=personal_info_window, text='login').grid(row=5)

    # Initialise screen
    personal_info_window.mainloop()

# Start function
personal_info_start()
