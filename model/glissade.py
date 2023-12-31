from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from car import Car
from battery.spindler_battery import SpindlerBattery

class Glissade():
    def __init__(self, current_mileage, last_service_mileage, last_service_date, current_date) -> Car:
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
