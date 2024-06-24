import heapq
from collections import deque
from sortedcontainers import SortedDict

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        res = 0
        
        for window in range(1, N+1):
            for i in range(N-window+1):
                temp = nums[i:i+window]
                if max(temp) - min(temp) <= limit:
                    res = window
                    break

        return res
    
    #TLE
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        res = 0
        l = 1
        r = N
        
        while l <= r:
            window = l + ((r-l) >> 1)
            is_true = False
            for i in range(N-window+1):
                temp = nums[i:i+window]
                if max(temp) - min(temp) <= limit:
                    res = window
                    is_true = True
                    break

            if is_true:
                res = window
                l = window + 1
            else:
                r = window - 1

        return res
    
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        max_hq = []
        min_hq = []
        res = 0
        l = 0

        for r in range(N):
            heapq.heappush(max_hq, [-nums[r], r])
            heapq.heappush(min_hq, [nums[r], r])

            while abs((max_hq[0][0] * -1) - min_hq[0][0]) > limit:
                l = min(max_hq[0][1], min_hq[0][1]) + 1

                while max_hq[0][1] < l:
                    heapq.heappop(max_hq)
                
                while min_hq[0][1] < l:
                    heapq.heappop(min_hq)

            res = max(res, r-l+1)

        return res
    

    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        window = SortedDict()
        l = 0
        res = 0

        for r in range(N):
            if nums[r] in window:
                window[nums[r]] += 1
            else:
                window[nums[r]] = 1

            while window.peekitem()[0] - window.peekitem(0)[0] > limit:

                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    window.pop(nums[l])
                l += 1
            
            res = max(res, r - l + 1)

        return res
    
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        res = 0
        l = 0
        min_q = deque()
        max_q = deque()

        for r in range(N):

            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
                
            max_q.append(nums[r])

            while min_q and min_q[-1] > nums[r]:
                min_q.pop()

            min_q.append(nums[r])
            
            while max_q[0] - min_q[0] > limit:

                if max_q[0] == nums[l]:
                    max_q.popleft()
                
                if min_q[0] == nums[l]:
                    min_q.popleft()
            
                l += 1
            res = max(res, r-l+1)
        
        return res
                





# print(Solution().longestSubarray([8,2,4,7], 2)) #2
# print(Solution().longestSubarray([10,1,2,4,7,2], 5)) #4
print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0)) #3
print(Solution().longestSubarray([1,5,6,7,8,10,6,5,6], 4)) #5