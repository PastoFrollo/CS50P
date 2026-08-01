import sys
from random import randint
from pyfiglet import Figlet
import pyfiglet

figlet = Figlet()


def main():
    phrase = input("Input: ")

    if len(sys.argv) == 1:
        figlet_random()
        figlet_print(phrase)
    elif len(sys.argv) == 3:
        figlet_config(sys.argv)
        figlet_print(phrase)
    else:
        sys.exit()


def figlet_random():
    fonts = figlet.getFonts()
    figlet.setFont(font = fonts[randint(0, len(fonts))])


def figlet_config(argv):
    try:
        if argv[1] == "-f" or argv[1] == "--font":
            figlet.setFont(font = argv[2])
        else:
            sys.exit()

    except pyfiglet.FontNotFound:
        sys.exit()


def figlet_print(text):
    print(figlet.renderText(text))


main()