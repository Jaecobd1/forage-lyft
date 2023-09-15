from battery.battery import Battery

class SpindlerBattery():
    def __init__(self, last_service_date, curent_date) -> Battery:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = curent_date
    def needs_service(self):
        return self.current_date - self.last_service_date > 10000
