import re
from enum import Enum
import string as stringImport
import random

# methods to check whether or not a string matches our specifications for that string.


def string(gui_input):
    """
    This method checks whether or not the input string contains only a-z (case insensitive),
    periods, apostrophes and spaces.
    :param gui_input: the input string, taken from the gui.
    :return: boolean of whether or not the string matches the regex.
    """
    return re.match("^[a-zA-Z.' ]+$", gui_input)


def huisNr(gui_input):
    """
    This method checks whether or not the input string contains only digits.
    :param gui_input: the input string, taken from the gui.
    :return: boolean of whether or not the string matches the regex.
    """
    return re.match("^\d+$", gui_input)


def postcode(gui_input):
    """
    This method checks whether or not the input string contains 4 digits, possibly a space in-between,
     followed by two letters.
    :param gui_input: the input string, taken from the gui.
    :return: boolean of whether or not the string matches the regex.
    """
    return re.match("^\d{4}\s?\w{2}$", gui_input)


def telNr(gui_input):
    """
    This method checks whether or not the input string contains 8 digits after the Dutch land code
    :param gui_input: the input string, taken from the gui.
    :return: boolean of whether or not the string matches the regex.
    """
    return re.match("^06-\d{8}$", gui_input)


# A class enumerating the different types of generatable codes. Used for clairvoyance in code.
class CodeType:
    DIGITS = 0
    LETTERS = 1
    ALL = 2


def makeRandomCode(length, typeOfCode):
    """
        Method for making a pseudo-randomized code.
    :param length: Specify the length of the code you want.
    :param typeOfCode: specify whether or not to use digits, letters or both.
    :return: returns the code as a string.
    """
    # randomizer can be seen as a 'char array' containing all characters we are to use in randomizing a code.
    randomizer = ""
    # Check if the requested type equals DIGITS
    if typeOfCode == CodeType.DIGITS:
        randomizer = stringImport.digits

    # Check if the requested type equals LETTERS
    elif typeOfCode == CodeType.LETTERS:
        randomizer = stringImport.ascii_uppercase

    # Check if the requested type equals ALL
    elif typeOfCode == CodeType.ALL:
        randomizer = stringImport.ascii_uppercase + stringImport.digits

    # Once we've gathered all necessary characters, we start creating the random code with a for-loop.
    randomCode = ""
    for i in range(length):
        # Each iteration we add one random character to our code
        randomCode += random.choice(randomizer)

    return randomCode

