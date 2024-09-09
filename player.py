import math
from person import Person
from person import Consts
from work_place import WorkPlace

class Player(Person):
    def __init__(self, name:str, age:int , money:int = 1000):
        super().__init__(name, age)
        self.__job = "player"
        self.__money:int = money
        self.__owned_places: list[WorkPlace] = []
        self.__employees: list[Person] = []

    def get_money(self) -> int:
        return self.__money
