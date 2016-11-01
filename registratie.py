import string
import random
import re


class CodeType:
    """
        TODO: ADD DOCUMENTATION HERE
    """
    DIGITS, LETTERS, ALL = 0,1,2


# CONSTANTS
RANDOM_ID_LENGTH = 8
RANDOM_CONFIRMATION_CODE_LENGTH = 6


def register(): # maybe we should change this name to a name that better explains what this functions does (e.g.: registerNewUser)
    """TODO: ADD DOCUMENTATION HERE!

    :return:
    """
    u_id = randomID() #Vague naming

    # We'll have to reprogram the remainder of this function to adjust to the GUI
    name = get_input("Typ uw volledige naam in: ", "^[a-zA-Z. ]+$")
    street = get_input("Typ uw straatnaam in: ", "^[a-zA-Z. ]+$")
    house_number = get_input("Typ uw huisnummer in: ", "^\d+$")
    postal_code = get_input("Typ uw postcode in: ", "^\d{4}\w{2}$")
    telnr = get_input("Typ uw telefoonnummer in: 06-", "^\d{8}$")

    securitycode = send_msg_to_nr(telnr)
    while input("Heeft u de code ontvangen? Y/N: ") == 'N':  # check to ensure user got a message on his phone
        telnr = get_input("Typ uw telefoonnummer in: 06-", "^\d{8}$")
        securitycode = send_msg_to_nr(telnr)

    while securitycode != input("Voer de code in die naar uw telefoon gestuurd is: "):  # Security code invalid
        securitycode = send_msg_to_nr(telnr)
        print("Code klopt niet. Er wordt een nieuwe verstuurd.")

    print("Code klopt. Registratie voltooid.")
    user = {'uid': u_id,
            'name': name,
            'street': street,
            'house_number': house_number,
            'postal_code': postal_code,
            'phone_number': telnr}
    # Database.Insert(user)


def get_input(console_output, pattern):  # this method receives what to output to console and a regex pattern.
    cmd_input = ""
    cmd_input = input(console_output)
    while not re.match(pattern, cmd_input):
        cmd_input = input("De invoer klopt niet. " + console_output)
    try:
        cmd_input = eval(cmd_input)  # Eval throws an exception when cmd_input is a string, that's why we're using try.
    # Eval is only done at the end because we need the input as a string at first to successfully match it with a regex.
    # Not using eval at all will not parse the input properly for our database.
    # So although this is dirty code, it's the only way.
    except:
        pass
    return cmd_input


def send_msg_to_nr(tel_nr):  # Sends an authentication message to the given number
    code = make_random_code(RANDOM_CONFIRMATION_CODE_LENGTH, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    # INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return code


def randomID():
    """TODO: ADD DOCUMENTATION HERE

    :return:
    """
    return make_random_code(RANDOM_ID_LENGTH, CodeType.DIGITS)


def make_random_code(length, type_of_code):
    """TODO: ADD DOCUMENTATION HERE

    :param length:
    :param type_of_code:
    :return:
    """
    # local variable to store the data type we want to randomize
    _randomizer = ""

    # Check if the Type of code refers to DIGITS only
    if type_of_code == CodeType.DIGITS:
        _randomizer = string.digits

    # Check if the Type of code refers to LETTERS only
    elif type_of_code == CodeType.LETTERS:
        _randomizer = string.ascii_uppercase

    # Check if the Type of code refers DIGITS and LETTERS combined
    elif type_of_code == CodeType.ALL:
        _randomizer = string.ascii_uppercase + string.digits

    random_code = ""
    for i in range(length):
        random_code += _randomizer[random.randint(0,len(_randomizer) - 1)]
    return random_code


# TEST CODE HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERE::::
register()
