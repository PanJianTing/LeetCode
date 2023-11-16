from collections import deque

class MovingAverage:
    def __init__(self, size) -> None:
        self.N = size
        self.cur = 0
        self.sum = 0
        self.q = deque()

    def next(self, val) -> float:
        if self.cur >= self.N:
            self.sum -= self.q.popleft()
            self.cur -= 1
        
        self.sum += val
        self.cur += 1
        self.q.append(val)
        return self.sum / self.cur
    

class MovingAverage:
    def __init__(self, size) -> None:
        self.N = size
        self.cur = 0
        self.vals = []

    def next(self, val) -> float:

        self.vals.append(val)
        self.cur = min(self.N, self.cur + 1)

        mysum = sum(self.vals[-self.cur:])
        
        return mysum / self.cur
    

class MovingAverage:
    def __init__(self, size) -> None:
        self.N = size
        self.h = 0
        self.sum = 0
        self.vals = [0] * self.N
        self.cnt = 0

    # from one idx
    def next(self, val) -> float:
        
        tal_idx = (self.h + 1) % self.N
        tal_val = self.vals[tal_idx]
        self.sum += val
        self.sum -= tal_val
        self.h = (self.h + 1) % self.N
        self.vals[self.h] = val
        self.cnt += 1
        
        return self.sum / min(self.cnt, self.N)
    
    # from zero idx
    def next(self, val) -> float:
        
        tal_val = self.vals[self.h]
        self.vals[self.h] = val
        self.sum += val
        self.sum -= tal_val
        self.h = (self.h + 1) % self.N
        self.cnt += 1
        
        return self.sum / min(self.cnt, self.N)
        

ma = MovingAverage(3)

print(ma.next(1))
print(ma.next(10))
print(ma.next(3))
print(ma.next(5))