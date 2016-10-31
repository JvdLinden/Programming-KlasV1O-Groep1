import string
import random
from enum import Enum


def registreren():
    uID = randomID()
    name = eval(input("Typ uw naam in: "))
    while type(name) is not str:
        name = eval(input("De invoer klopt niet. Typ uw naam in: "))
    address = eval(input("Typ uw adres in (straatnaam, huisnummer, postcode): "))
    while type(address) is not str:
        address = eval(input("De invoer klopt niet. Typ uw adres in (straatnaam, huisnummer, postcode): "))
    telnr = get_telephone_nr()
    securitycode = send_msg_to_nr(telnr)
    while input("Heeft u de code ontvangen? Y/N") == 'N':
        telnr = get_telephone_nr()
        securitycode = send_msg_to_nr(telnr)
    while securitycode != input("Voer de code in die naar uw telefoon gestuurd is: "):  # Security code invalid
        securitycode = send_msg_to_nr(telnr)
        print("Code klopt niet. Er wordt een nieuwe verstuurd.")
    print("Code klopt. Registratie voltooid.")
    


def get_telephone_nr():
    telnr = eval(input("Typ uw telefoonnummer in: 06-"))
    while type(telnr) is not int or len(telnr) != 8:
        telnr = eval(input("De input klopt niet. Typ uw telefoonnummer in: 06-"))
    return telnr


def send_msg_to_nr(tel_nr):  # Sends an authentication message to the given number
    code = make_random_code(6, Random.ALL)
    # TELEGRAM SEND MESSAGE WITH 'code' IN IT RIIIIIIIIGHT HEEEEEEEEEEEEEEEERE
    print(code)
    #INSTEAD, IMMA USE THIS PRINT IN THE MEANWHILE
    return code


def randomID():
    return make_random_code(8, Random.DIGITS)


class Random(Enum):
    DIGITS = 0
    LETTERS = 1
    ALL = 2


def make_random_code(length, type_of_code):
    randomizer = ""
    if type_of_code.value == 0:
        randomizer.add(string.digits)
    elif type_of_code.value == 1:
        randomizer.add(string.ascii_uppercase)
    elif type_of_code.value == 2:
        randomizer.add(string.ascii_uppercase)
        randomizer.add(string.digits)
    random_code = ""
    for i in range(0, length):
        randomint = random.randint(0, len(randomizer))
        random_code.add(randomizer[randomint])
    return random_code