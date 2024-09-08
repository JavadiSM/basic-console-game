from person import Person 


class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:

    def __init__(self, name: str):
        pass

    def get_price(self) -> int:
        pass

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        pass

    def hire(self, person: Person):
        pass

    def get_expertise(self) -> str:
        pass

    def calc(self) -> int:
        pass

    @staticmethod
    def calc_all() -> int:
        pass
