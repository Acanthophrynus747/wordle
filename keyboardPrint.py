from termcolor import colored

def showKeyboard(not_present):

    line_1 = "QWERTYUIOP"
    line_2 = "ASDFGHJKL"
    line_3 = "ZXCVBNM"

    letter_color = "white"
    present_format = "on_green"
    not_present_format = "on_red"

    for i in line_1:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")

    print("")

    for i in line_2:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")

    print("")
    print(" ", end = "")

    for i in line_3:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")
    print("")