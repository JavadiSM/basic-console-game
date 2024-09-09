import math
from person import Person
from person import Consts
from work_place import WorkPlace
from game_elements import GameElements
class Player(Person):
    def __init__(self, name:str, age:int , money:int = 1000):
        super().__init__(name, age)
        self.__job = "player"
        self.__money:int = money
        self.__owned_places: list[WorkPlace] = []
        self.__employees: list[Person] = []
        self.game_elements: GameElements = GameElements(self)

    def get_money(self) -> int:
        return self.__money
    
    def buy_place():
        pass
