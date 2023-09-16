from serviceable import Serviceable
from tire.octoprime_tire import OctoPrime
from tire.carrigan_tire import CarriganTire

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        self.tires = CarriganTire(0, 0, 0, 0)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

    def add_carrigan_tires(self, p1, p2, p3, p4):
        self.tires = CarriganTire(p1, p2, p3, p4)

    def add_octoprime_tires(self, p1, p2, p3, p4):
        self.tires = OctoPrime(p1, p2, p3, p4)


    def remove_tires(self):
        self.tires = []

