class PetrolEngine:
    def start(self):
        print("Petrol Engine is starting..")


class Vehicle:
    def __init__(self, engine: PetrolEngine):
        self.engine = engine

    def engine_start(self):
        self.engine.start()

    def accelerate(self):
        print("accelerating..")

p = PetrolEngine()
car1 = Vehicle(p)
car1.engine_start()
car1.accelerate()
