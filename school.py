import math
from work_place import WorkPlace
from work_place import Consts


class School(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = math.floor(math.sqrt(self.level))

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * math.floor(math.sqrt(self.level))