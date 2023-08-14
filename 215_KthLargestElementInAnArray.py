import heapq
import random

class Solution:
    # heap
    def findKthLargest(self, nums, k) -> int:

        hq = []

        for num in nums:
            heapq.heappush(hq, -num)
        
        for i in range((k-1)):
            heapq.heappop(hq)

        return hq[0] * -1
    
    # sort
    def findKthLargest(self, nums, k) -> int:

        nums.sort()
        return nums[-k]
    
    # heap
    def findKthLargest(self, nums, k) -> int:

        hq = []

        for num in nums:
            heapq.heappush(hq, num)
            if len(hq) > k:
                heapq.heappop(hq)

        return hq[0]
    
    # quick select
    def findKthLargest(self, nums, k) -> int:

        def quickSelect(curNums, currK) -> int:
            N = len(curNums)
            checkN = random.choice(curNums)

            left, mid, right = [], [], []

            for n in curNums:
                if n < checkN:
                    left.append(n)
                elif n == checkN:
                    mid.append(n)
                else:
                    right.append(n)

            if currK <= len(right):
                return quickSelect(right, currK)
            elif len(right) + len(mid) < currK:
                return quickSelect(left, currK - len(right) - len(mid))

            return checkN
        return quickSelect(nums, k)
    
    # Count
    def findKthLargest(self, nums, k) -> int:

        minN = min(nums)
        maxN = max(nums)
        count = [0] * ((maxN - minN) + 1)
        

        for n in nums:
            count[n-minN] += 1
        
        for i in range(len(count)-1, -1, -1):
            k = k - count[i]
            if k <= 0:
                return minN + i
        
        return -1


        


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))

        
