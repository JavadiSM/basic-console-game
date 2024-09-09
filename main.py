import os
import re
from cmd_color_printer import ColorPrinter, print_hat
def main():
    os.system("cls")
    print_hat()
    ColorPrinter.colored_print("enter your name")
    while not re.match("^exit$",user_command:=input()):
        print("oops, your command are unkown, try again")
    os.system("cls")


if __name__ == "__main__":
    main()