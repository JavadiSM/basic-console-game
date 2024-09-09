from person import Person


class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {"mine": 300, "school": 100, "company": 200}
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10


class WorkPlace:
    instances: list = []  # static variable

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.level: int = 1
        self.expertise: str = ""
        self.employees: list = []
        self.capacity: int = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self) -> None:
        pass

    def calc_capacity(self) -> None:
        pass

    def upgrade(self) -> None:
        self.level += 1
        self.calc_capacity()

    def hire(self, person: Person) -> None:
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
    
    def __str__(self) -> str:
        return f"{self.expertise} {self.name}"
