from abc import ABC

class tire(ABC):
    def __init__(self, p1, p2, p3, p4):
        self.pressure = [p1, p2, p3, p4]
    def needs_service(self):
        pass
