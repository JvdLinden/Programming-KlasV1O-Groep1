import re


def string(gui_input):
    return re.match("[a-zA-Z.' ]+", gui_input)


def huis_nr(gui_input):
    return re.match("\d+", gui_input)


def postcode(gui_input):
    return re.match("\d{4}\w{2}", gui_input)


def tel_nr(gui_input):
    return re.match("06-\d{8}$", gui_input)



