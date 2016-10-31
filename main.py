def registreren():
    uID = randomID()
    name = eval(input("Typ uw naam in: "))
    while type(name) is not str:
        name = eval(input("De invoer klopt niet. Typ uw naam in: "))
    address = eval(input("Typ uw adres in: "))
    while type(address) is not str:
        address = eval(input("De invoer klopt niet. Typ uw adres in: "))
    get_telephone_nr()


def get_telephone_nr():
    telnr = eval(input("Typ uw telefoonnummer in: 06-"))
    while type(telnr) is not int or len(telnr) != 8:
        telnr = eval(input("De input klopt niet. Typ uw telefoonnummer in: 06-"))
    return telnr