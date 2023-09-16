from tire.tire import tire

class CarriganTire(tire):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3, p4)

    def needs_service(self):
        for i in self.pressure:
            if(i >= 0.9):
                return True
        return False
