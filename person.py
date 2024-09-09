import math


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {"worker": 200, "teacher": 150, "engineer": 250}
    BASE_COST = {"worker": 200, "teacher": 150, "engineer": 300}
    BASE_INCOME = {
        "worker": {"mine": 800, "school": 500, "company": 600},
        "teacher": {"mine": 400, "school": 900, "company": 700},
        "engineer": {"mine": 1000, "school": 800, "company": 900},
    }
    MIN_AGE = 5
    AGE_MUL = 5


class Person:
    instances: list = []

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: str = age
        self.level: int = 1
        self.work_place = None
        self.job: str = ""
        Person.instances.append(self)

    def do_level(self, income) -> int:
        return income * math.sqrt(self.work_place.level * self.level)

    def calc_income(self) -> None:
        pass

    def calc_life_cost(self) -> None:
        pass

    def calc(self) -> int:
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self) -> str:
        return self.job

    def upgrade(self) -> None:
        self.level += 1

    @staticmethod
    def calc_all() -> int:
        return sum([person.calc() for person in Person.instances])
    
    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.job}"
