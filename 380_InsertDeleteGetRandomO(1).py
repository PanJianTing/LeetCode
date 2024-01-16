from collections import defaultdict
from random import randint



class RandomizedSet:

    def __init__(self):
        self.num_set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.num_set:
            return False
        self.num_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.num_set:
            self.num_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        idx = randint(0, len(self.num_set)-1)
        return list(self.num_set)[idx]
    
    
class RandomizedSet:

    def __init__(self):
        self.num_dict = defaultdict(int)
        self.num_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False

        self.num_dict[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.num_dict:
            idx = self.num_dict[val]
            self.num_list[idx], self.num_list[-1] = self.num_list[-1], self.num_list[idx]
            self.num_dict[self.num_list[idx]] = idx
            self.num_list.pop()
            del self.num_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        idx = randint(0, len(self.num_list)-1)
        return self.num_list[idx]

        


obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())