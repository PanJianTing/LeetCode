from collections import defaultdict

class ParkingSystem:

    typeDic = defaultdict(int)

    def __init__(self, A: int, B: int, C: int):

        self.typeDic = defaultdict(int)
        self.typeDic[1] = A
        self.typeDic[2] = B
        self.typeDic[3] = C

    def addCar(self, t: int) -> bool:
        if self.typeDic[t] > 0:
            self.typeDic[t] -= 1
            return True
        return False
    

class ParkingSystem:

    parkings = []

    def __init__(self, A, B, C):
        self.parkings = [A, B, C]
    
    def addCar(self, t) -> bool:
        self.parkings[t-1] -= 1
        return self.parkings[t-1] >= 0

