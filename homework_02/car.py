"""
создайте класс `Car`, наследник `Vehicle`
"""
from . import base
from engine import Engine


class Car(base.Vehicle):
    engine = None
    
    def set_engine(self, engine: Engine):
        self.engine = engine
