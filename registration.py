import string
import random
from enum import Enum


class CodeType(Enum):
    DIGITS = 0
    LETTERS = 1
    ALL = 2


class Info(Enum):
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4

# CONSTANTS
RANDOM_ID_LENGTH = 8
RANDOM_CONFIRMATION_CODE_LENGTH = 6


# ToDo : Finish Comments / Documentation!
def add_to_database(data):
    """

    :param data:
    :return:
    """
    '''
    This block of code will be the database transition
        {'sticker': randomID(),
            'name': data['name'],
            'street': data['street'],
            'house_number': data['house_number'],
            'postal_code': data['postal_code'],
            'phone_number': data['phone_number']}
    '''
    pass


# ToDo : Finish Comments / Documentation!
def send_msg_to_nr(tel_nr):
    """Sends an authentication message to the given number

    :param tel_nr:
    :return:
    """
    confirmation_code = make_random_code(RANDOM_CONFIRMATION_CODE_LENGTH, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(confirmation_code)
    # INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return confirmation_code


# ToDo : Finish Comments / Documentation!
def randomID():
    """TODO: ADD DOCUMENTATION HERE

    :return:
    """
    return make_random_code(RANDOM_ID_LENGTH, CodeType.DIGITS)


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
        _randomizer = string.digits

    # Check if the requested type equals LETTERS
    elif type_of_code == CodeType.LETTERS:
        _randomizer = string.ascii_uppercase

    # Check if the requested type equals ALL
    elif type_of_code == CodeType.ALL:
        _randomizer = string.ascii_uppercase + string.digits

    _randomCode = ""
    # ToDo : add documentation
    for i in range(length):
        _randomInteger = random.randint(0, len(_randomizer) - 1)
        _randomCode += _randomizer[_randomInteger]

    return _randomCode
