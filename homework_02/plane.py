"""
создайте класс `Plane`, наследник `Vehicle`
"""
from . import base
from homework_02.exceptions import CargoOverload


class Plane(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if self.cargo+weight <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        last_value = self.cargo
        self.cargo = 0
        return last_value



