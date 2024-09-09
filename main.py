import os
import re
from cmd_color_printer import ColorPrinter, print_hat
from player import Player
from work_place import *
from mine import Mine
from school import School
from company import Company
from person import Person
from teacher import Teacher
from engineer import Engineer
from worker import Worker
import random

"""
it is clear that the way I import them is not effivent and it is time consuming.
this will be fixed once the game basics are implemented
"""


def main():
    os.system("cls")
    print_hat()

    #initialzing player
    ColorPrinter.colored_print("enter your character in game name","red")
    name:str = input()
    ColorPrinter.colored_print("enter your character in game name","blue")
    age:int = int(input())
    player:Player = Player(name,age)

    while not re.match("^exit$",user_command:=input()):

        print("oops, your command are unkown, try again")
    os.system("cls")


if __name__ == "__main__":
    main()