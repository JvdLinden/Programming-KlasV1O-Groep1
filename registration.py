from Validate import *


class Info(Enum):  # Class specifying in what order the information during registration is processed
    NAME = 0
    STREET = 1
    HOUSE_NR = 2
    POSTAL_CODE = 3
    PHONE_NR = 4

# CONSTANTS
RANDOM_ID_LENGTH = 8
RANDOM_CONFIRMATION_CODE_LENGTH = 6


def add_to_database(database, data):
    """

    :param database: instance of a database handler
    :param data: dictionary containing relevant data for registration
    :return: whether the method succeeded or not
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
    return False


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

