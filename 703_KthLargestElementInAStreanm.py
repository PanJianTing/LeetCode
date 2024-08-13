import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.k_list = nums
        self.k_list.sort()


    def add(self, val: int) -> int:
        if len(self.k_list) == 0 or self.k_list[-1] <= val:
            self.k_list.append(val)
            return self.k_list[-self.k]

        self.k_list.append(val)
        self.k_list.sort()
        return self.k_list[-self.k]
    

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.hq = []
        
        for n in nums:
            heapq.heappush(self.hq, n)
        
        while self.hq and len(self.hq) > k:
            heapq.heappop(self.hq)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)

        while len(self.hq) > self.k:
            heapq.heappop(self.hq)
        
        return self.hq[0]


# temp = KthLargest(3, [4, 5, 8, 2])

# print(temp.add(3))
# print(temp.add(5))
# print(temp.add(10))
# print(temp.add(9))
# print(temp.add(4))



temp = KthLargest(2, [0])

print(temp.add(-1))
print(temp.add(1))
print(temp.add(-2))
print(temp.add(-4))
print(temp.add(3))

