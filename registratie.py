import string
import random
import re
from enum import Enum


def registreren():
    u_id = randomID()
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
    code = make_random_code(6, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    # INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return code


def randomID():
    return make_random_code(8, CodeType.DIGITS)


class CodeType(Enum):
    DIGITS = 0
    LETTERS = 1
    ALL = 2


def make_random_code(length, type_of_code):
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
# TEST CODE HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERE::::
registreren()