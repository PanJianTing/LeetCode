import heapq
from sortedcontainers import SortedSet

class SeatManager:
    def __init__(self, n: int):

        self.all_seat = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        return heapq.heappop(self.all_seat)

    def unreserve(self, n):
        heapq.heappush(self.all_seat, n)


class SeatManager:
    def __init__(self, n):
        self.now = 1
        self.q = []

    def reserve(self) -> int:
        if self.q:
            return heapq.heappop(self.q)
        
        res = self.now
        self.now += 1
        return res
    
    def unreserve(self, n):
        heapq.heappush(self.q, n)

class SeatManager:

    def __init__(self, n):
        self.now = 1
        self.set = SortedSet()

    def reserve(self) -> int:
        if self.set:
            return self.set.pop(0)

        res = self.now
        self.now += 1
        return res

    def unreserve(self, n):
        self.set.add(n)

        