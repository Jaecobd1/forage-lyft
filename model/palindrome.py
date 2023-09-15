from datetime import datetime

from engine.sternman_engine import SternmanEngine
from car import Car
from battery.spindler_battery import SpindlerBattery


class Palindrome():
    def __init__(self,
                 current_date,
                last_service_date,
                warning_light_on,
                ) -> Car:
        super().__init__(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
