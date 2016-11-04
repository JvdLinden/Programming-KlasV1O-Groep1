from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler, combinedHandler, telegramHandler
from tkinter import *
from enum import Enum


class Info:  # Class specifying in what order the information during registration is processed
    ID = 0
    NAME = 1
    STREET = 2
    HOUSE_NR = 3
    POSTAL_CODE = 4
    PHONE_NR = 5
    REG_KEY = 6
    CHAT_ID = 7
    BIKE_KEY = 8

class PersonalInfo(object):
    def __init__(self, cb, master):
        """
        Create GUI for personal information after validation

        :return: Returns a GUI Screen
        """
        usval = UserValidator(cb, master)
        _user = usval.getValue()
        del usval
        if not _user:
            return
        else:
            userInfo = cb.retrievePersonalData(_user)[0]  # Return value of retrievePersonalData is a list containing
            # a tuple containing user info in order specified in Info enum
            # Create a windows to show personal information
            personalInfoWindow = Tk()

            # Title for personal information window
            personalInfoWindow.title('Persoonlijke informatie')

            # Text om head of page
            nameLabel = Label(master=personalInfoWindow, text='Naam: %s' % userInfo[Info.NAME]).grid(row=0, sticky=W)
            streetLabel = Label(master=personalInfoWindow, text='Straat: %s' % userInfo[Info.STREET]).grid(row=1, sticky=W)
            houseNrLabel = Label(master=personalInfoWindow, text='Huisnr.: %s' % userInfo[Info.HOUSE_NR]).grid(row=2, sticky=W)
            postalCodeLabel = Label(master=personalInfoWindow, text='Postcode: %s' % userInfo[Info.POSTAL_CODE]).grid(row=3, sticky=W)
            phoneNrLabel = Label(master=personalInfoWindow, text='Tel.Nr.: %s' % userInfo[Info.PHONE_NR]).grid(row=4, sticky=W)
            bikeKeyLabel = Label(master=personalInfoWindow, text='Pers.Code: %s' % userInfo[Info.BIKE_KEY]).grid(row=5, sticky=W)

            backButton = Button(master=personalInfoWindow, text=Constants.BACK, command=personalInfoWindow.destroy).grid(column=1)

