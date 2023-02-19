from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine is starting..")


class HybridEngine(Engine):
    def start(self):
        print("Hybrid engine is starting..")


class Vehicle:
    def __init__(self, engine: Engine):
        self.engine = engine

    def engine_start(self):
        self.engine.start()

    def accelerate(self):
        print("accelerating..")

p = PetrolEngine()
car1 = Vehicle(p)
car1.engine_start()
car1.accelerate()

h = HybridEngine()
car2 = Vehicle(h)
car2.engine_start()
car2.accelerate()
