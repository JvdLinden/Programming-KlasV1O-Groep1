from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler, combinedHandler
from tkinter import *



def Personal_info_validation(cb):
    """
    Show screen for input personal code and the security code
    :return:
    """

    # Create validator object
    validator = UserValidator(cb)

    # when the validator object is done running, retrieve the value.
    validation = validator.getValue()

    # Check if validation is succesfull or not
    if validation != False:
        personal_info_screen()

    # ToDo: add Error message????
    else:
        pass


def personal_info_screen(cb):

    """
    Create GUI for personal information after validation

    :return: Returns a GUI Screen
    """
    # Create a windows to show personal information
    personal_info_window = Tk()

    # Title for personal information window
    personal_info_window.title('Persoonlijke informatie')

    # Text om head of page
    name_label = Label(master=personal_info_window, text='Persoonlijke informatie').grid(row=0)

    # ToDo : Add personal info from Database
    cb.retrievePersonalData()



personal_info_screen()
