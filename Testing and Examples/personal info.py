from tkinter import *
from enum import Enum
import registration
import Validate


    # "SELECT * FROM users WHERE personal_code = {}".format(personalcode)

def personal_info_start():
    #Get users personal info
    #Create GUI for personal info page

# Default settings:
    global personal_info_window
    personal_info_window = Tk()
    personal_info_window.title("Persoonlijke informatie")

# widget creation
    name_label = Label(master=personal_info_window, text='Persoonlijke ID: ').grid(row=0)
    personal_id = Entry(master=personal_info_window).grid(row=1)
    submit_button = Button(master=personal_info_window, text='submit').grid(row=2)
    name_Label2 = Label(master=personal_info_window, text='Persoonlijke code: ').grid(row=3)
    personal_code = Entry(master=personal_info_window).grid(row=4)
    submit_button = Button(master=personal_info_window, text='login').grid(row=5)

    #Start loop
    personal_info_window.mainloop()

#Start function
personal_info_start()
