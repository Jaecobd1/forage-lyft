from datetime import datetime

from engine.capulet_engine import CapuletEngine
from car import Car
from battery.spindler_battery import SpindlerBattery


class Calliope():
    def __init__(self, current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
