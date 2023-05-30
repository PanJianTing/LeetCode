class MyHashSet:

    hashSet = set()

    def __init__(self) -> None:
        self.hashSet = set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet.remove(key)
    
    def contains(self, key: int) -> bool:
        return key in self.hashSet
        
class MyHashSet:

    keys = []
    
    def __init__(self):
        self.keys = []
        return None
    
    def add(self, key: int) -> None:
        if key not in self.keys:
            self.keys.append(key)

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.keys:
            return True
        return False
    

class MyHashSet:

    keyRange = 769
    bucketList = []

    def __init__(self) -> None:
        self.keyRange = 769
        self.bucketList = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange
    
    def add(self, key):

        idx = self._hash(key)
        self.bucketList[idx].insert(key)

    def remove(self, key):
        idx = self._hash(key)
        self.bucketList[idx].delete(key)

    def contains(self, key):
        idx = self._hash(key)
        return self.bucketList[idx].exists(key)

    

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Bucket:
    head = None
    def __init__(self) -> None:
        self.head = Node(0)

    def insert(self, val):
        if self.exists(val) == False:
            new = Node(val, self.head.next)
            self.head.next = new


    def delete(self, val):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
    

class MyHashSet:
    def eval_hash(self, key):
        return ((key * 1031237) & (1 << 20) - 1) >> 5

    def __init__(self) -> None:
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int):
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)
    
    def remove(self, key):
        idx = self.eval_hash(key)
        if key in self.arr[idx]:
            self.arr[idx].remove(key)

    def contains(self, k):
        return k in self.arr[self.eval_hash(k)]
