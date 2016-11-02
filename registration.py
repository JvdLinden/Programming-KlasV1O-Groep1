import string
import random
import re
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

_myDict = {
    'name': 'naampje',
    'street' : 'straatje',
}

# CONSTANTS
RANDOM_ID_LENGTH = 8
RANDOM_CONFIRMATION_CODE_LENGTH = 6


# ToDo : Finish Comments / Documentation!
def is_valid(data):
    """

    :param data:
    :return:
    """
    if not re.match("^[\p{L}\s.']+$", data[Info.NAME.value]):
        return False, "naam"
    elif not re.match("^[\p{L}\s.']+$", data[Info.STREET.value]):
        return False, "straatnaam"
    elif not re.match("^\d+$", data[Info.HOUSE_NR.value]):
        return False, "huisnummer"
    elif not re.match("^\d{4}\w{2}$", data[Info.POSTAL_CODE.value]):
        return False, "postcode"
    elif not re.match("^\d{8}$", data[Info.PHONE_NR.value]):
        return False, "telefoonnummer"
    else:
        return True, ""

'''
This block of code will be the database transition
    {'uid': randomID(),
        'name': data[Info.NAME],
        'street': data[Info.STREET],
        'house_number': data[Info.HOUSE_NR],
        'postal_code': data[Info.POSTAL_CODE],
        'phone_number': data[Info.PHONE_NR]}
'''


# ToDo : Finish Comments / Documentation!
def add_to_database(data):
    """

    :param data:
    :return:
    """
    pass


# ToDo : Finish Comments / Documentation!
def send_msg_to_nr(tel_nr):
    """Sends an authentication message to the given number

    :param tel_nr:
    :return:
    """
    code = make_random_code(RANDOM_CONFIRMATION_CODE_LENGTH, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    # INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return code


# ToDo : Finish Comments / Documentation!
def randomID():
    """TODO: ADD DOCUMENTATION HERE

    :return:
    """
    return make_random_code(RANDOM_ID_LENGTH, CodeType.DIGITS)


# ToDo : Finish Comments / Documentation!
def make_random_code(length, type_of_code):
    """ToDo: ADD DOCUMENTATION HERE

    :param length:
    :param type_of_code:
    :return:
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
