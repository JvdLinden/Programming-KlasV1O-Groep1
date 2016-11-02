import re
from enum import Enum
import string as stringImport
import random

def string(gui_input):
    return re.match("[a-zA-Z.' ]+", gui_input)


def huis_nr(gui_input):
    return re.match("\d+", gui_input)


def postcode(gui_input):
    return re.match("\d{4}\w{2}", gui_input)


def tel_nr(gui_input):
    return re.match("06-\d{8}$", gui_input)

class CodeType(Enum):
    DIGITS = 0
    LETTERS = 1
    ALL = 2

# ToDo : Finish Comments / Documentation!
def make_random_code(length, type_of_code):
    """
        Method for making a pseudo-randomized code.
    :param length: Specify the length of the code you want.
    :param type_of_code: specify whether or not to use digits, letters or both.
    :return: returns the code as a string.
    """
    _randomizer = ""
    # Check if the requested type equals DIGITS
    if type_of_code == CodeType.DIGITS:
        _randomizer = stringImport.digits

    # Check if the requested type equals LETTERS
    elif type_of_code == CodeType.LETTERS:
        _randomizer = stringImport.ascii_uppercase

    # Check if the requested type equals ALL
    elif type_of_code == CodeType.ALL:
        _randomizer = stringImport.ascii_uppercase + stringImport.digits

    _randomCode = ""
    # ToDo : add documentation

    for i in range(length):
        _randomCode += random.choice(_randomizer)

    return _randomCode

