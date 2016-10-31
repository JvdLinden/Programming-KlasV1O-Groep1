import string
import random
from enum import Enum


def registreren():
    name = get_input("Typ uw volledige naam in: ", str)
    street = get_input("Typ uw straatnaam in: ",str)
    house_number = get_input("Typ uw huisnummer in: ", int)
    postal_code = get_input("Typ uw postcode in: ", str)
    telnr = get_telephone_nr()
    securitycode = send_msg_to_nr(telnr)
    while input("Heeft u de code ontvangen? Y/N: ") == 'N':
        telnr = get_telephone_nr()
        securitycode = send_msg_to_nr(telnr)
    while securitycode != input("Voer de code in die naar uw telefoon gestuurd is: "):  # Security code invalid
        securitycode = send_msg_to_nr(telnr)
        print("Code klopt niet. Er wordt een nieuwe verstuurd.")
    print("Code klopt. Registratie voltooid.")
    user = {'name': name, 'street': street, 'house_number': house_number, 'postal_code': postal_code, 'phone_number': telnr}
    # Database.Insert(user)


def get_input(console_output, type_of_input):
    cmd_input = ""
    try:
        cmd_input = eval(input(console_output))  # Eval throws an exception when cmd_input is a string
        while type(cmd_input) is not type_of_input:
            cmd_input = eval(input("De invoer klopt niet. " + console_output))
    except:
        pass
    return cmd_input


def get_telephone_nr():
    telnr = input("Typ uw telefoonnummer in: 06-")
    while type(eval(telnr)) is not int or len(telnr) != 8:
        telnr = eval(input("De input klopt niet. Typ uw telefoonnummer in: 06-"))
    return telnr


def send_msg_to_nr(tel_nr):  # Sends an authentication message to the given number
    code = make_random_code(6, CodeType.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    #INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
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
        random_int = random.randint(0, len(randomizer))
        random_code = random_code + randomizer[random_int]
    return random_code
# TEST CODE HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERE::::
registreren()