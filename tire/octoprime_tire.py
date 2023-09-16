from tire.tire import tire
from utils import array_sum

class OctoPrime(tire):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3, p4)
    def needs_service(self):
        if(array_sum(self.pressure) >= 3):
            return True
        else:
            return False
