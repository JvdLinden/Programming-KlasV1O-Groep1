from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler
from tkinter import *

def stallenValidation():
    """
    Show screen for input personal code and the security code
    :return:
    """
    # Create Database handler object
    dbHandler = databaseHandler.DatabaseHandler(Constants.DATABASE_MASK)

    # Create validator object
    validator = UserValidator(dbHandler)

    # when the validator object is done running, retrieve the value.
    validation = validator.getValue()

    # Check if validation is succesfull or not
    if validation != False:



    else:
        pass

def stallen_screen():
    # Create a window to show personal information
    stallen_window = Tk()

    # Title for personal information window
    stallen_window.title('Stallen')


