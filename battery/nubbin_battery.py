from battery.battery import Battery

class NubbinBattery():
    def __init__(self, last_service_date, curent_date) -> Battery:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = curent_date
