class MyHashMap:
    
    def __init__(self) -> None:
        self.valMap = {}

    def put(self, key, value) -> None:
        self.valMap[key] = value
    
    def get(self, key) -> int:
        return self.valMap[key] if key in self.valMap else -1

    def remove(self, key) -> None:
        if key in self.valMap:
            del self.valMap[key]


class MyHashMap:

    def __init__(self) -> None:
        self.vals = []

    def put(self, k, v):
        for i in range(len(self.vals)):
            key, _ = self.vals[i]
            if k == key:
                self.vals[i] = (k, v)
                return
        self.vals.append((k,v))
    
    def get(self, key) -> int:
        for k, v in self.vals:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        for i in range(len(self.vals)):
            k, _ = self.vals[i]
            if k == key:
                self.vals[i] = (k, -1)
                break
                

class MyHashMap:

    def __init__(self):
        self.modulo = 1024
        self.vals = [[]] * self.modulo

    def hashFunc(self, k):
        return (k // self.modulo, k % self.modulo)


    def put(self, k, v):
        k1, k2 = self.hashFunc(k)

        if not self.vals[k1]:
            self.vals[k1] = [-1] * self.modulo
        
        self.vals[k1][k2] = v

    def get(self, k):
        k1, k2 = self.hashFunc(k)

        if not self.vals[k1]:
            return -1
        
        return self.vals[k1][k2]
    
    def remove(self, k):
        k1, k2 = self.hashFunc(k)

        if self.vals[k1]:
            self.vals[k1][k2] = -1
        