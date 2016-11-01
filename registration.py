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

# CONSTANTS
RANDOM_ID_LENGTH = 8
RANDOM_CONFIRMATION_CODE_LENGTH = 6


def is_valid(data):
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


def add_to_database(data):
    pass


def send_msg_to_nr(tel_nr):  # Sends an authentication message to the given number
    code = make_random_code(6, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    # INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return code


def randomID():
    """TODO: ADD DOCUMENTATION HERE

    :return:
    """
    return make_random_code(8, CodeType.DIGITS)


def make_random_code(length, type_of_code):
    """TODO: ADD DOCUMENTATION HERE

    :param length:
    :param type_of_code:
    :return:
    """
    randomizer = ""
    if type_of_code.value == 0:
        randomizer = string.digits
    elif type_of_code.value == 1:
        randomizer = string.ascii_uppercase
    elif type_of_code.value == 2:
        randomizer = string.ascii_uppercase + string.digits
    random_code = ""
    for i in range(0, length):
        random_int = random.randint(0, len(randomizer) - 1)
        random_code += randomizer[random_int]
    return random_code
