import heapq
import bisect

class KthLargest:
    numList = []
    k = 0

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.numList = nums
        heapq.heapify(self.numList)
        while len(self.numList) > self.k:
            heapq.heappop(self.numList)

    def add(self, val: int) -> int:
        if len(self.numList) < self.k:
            heapq.heappush(self.numList, val)
        elif val > self.numList[0]:
            heapq.heapreplace(self.numList, val)
        return self.numList[0]
        


class KthLargest_my:
    
    numList = []
    k = 0

    def __init__(self, k: int, nums: list[int]):
        self.k = k - 1
        self.numList = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.numList.append(val)
        self.numList = sorted(self.numList, reverse=True)
        return self.numList[self.k]
    
class KthLargest:
    k = -1
    nums = []
    
    def __init__(self, k: int, nums: list[int]):
        self.k = -k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:

        idx = bisect.bisect_left(self.nums, val)
        self.nums.insert(idx, val)


        return self.nums[self.k]
    
class KthLargest:
    k = -1
    nums = []

    def __init__(self, k: int, nums: list[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

        while len(self.nums) > k:
            heapq.heappop(self.nums)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

k = KthLargest(3, [4,5,8,2])

print(k.add(3))
print(k.add(5))
print(k.add(10))
print(k.add(9))
print(k.add(4))