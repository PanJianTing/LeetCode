from collections import deque, defaultdict

class FirstUnique:

    def __init__(self, nums: list[int]):
        self.q = deque()
        self.cnt_map = defaultdict(int)

        for n in nums:
            self.add(n)
        
    def showFirstUnique(self) -> int:

        while self.q and self.cnt_map[self.q[0]] != 1:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, val: int) -> None:
        if val not in self.cnt_map:
            self.q.append(val)
        self.cnt_map[val] += 1



        