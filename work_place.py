from person import Person 


class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    instances = [] #static variable

    def __init__(self, name: str):
        self.name:str = name
        self.level:int = 1
        self.expertise:str = ""
        self.employees:list = []
        self.capacity:int = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level +=1
        self.calc_capacity()

    def hire(self, person: Person):
        if len(self.employees) == self.capacity:
            raise WorkPlaceIsFull()
        else:
            person.work_place = self
            self.employees.append(person)

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -1 * self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        return sum([workplace.calc() for workplace in WorkPlace.instances])
