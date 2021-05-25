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
        
