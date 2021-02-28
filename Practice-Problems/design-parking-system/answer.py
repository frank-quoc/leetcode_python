class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_counter = {1:big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.parking_counter[carType] > 0:
            self.parking_counter[carType] -= 1
            return True
        return False
