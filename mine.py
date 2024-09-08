from work_place import WorkPlace
from work_place import Consts


class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = self.level ** 2

    def calc_costs(self):
        return Consts.BASE_PLACE_COST + self.level * Consts.LEVEL_MUL