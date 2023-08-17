from collections import deque
import heapq

class Solution:
    
    def maxSlidingWindow(self, nums, k) -> list[int]:
        N = len(nums)
        l = 0
        r = k
        res = []

        for i in range(r, N+1):
            res.append(max(nums[l:r]))
            l += 1
            r += 1
        return res
    
    # wrong case #3
    def maxSlidingWindow(self, nums, k) -> list[int]:
        N = len(nums)
        q = deque()
        q.append(0)
        res = []

        for i in range(1, k):
            if nums[i] >= nums[q[0]]:
                q = deque()
                q.append(i)
            else:
                q.append(i)

        res.append(nums[q[0]])
        for i in range(k, N):
            # if i - k >= q[0]:
            while q and i - k >= q[0]:
                q.popleft()
            
            for j in range(len(q)-1, -1, -1):
                if nums[i] > nums[q[j]]:
                    q.pop()
            q.append(i)
            res.append(nums[q[0]])
        
        return res
    
    def maxSlidingWindow(self, nums, k) -> list[int]:
        N = len(nums)
        q = deque()
        res = []

        for i in range(0, k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])
        for i in range(k, N):
            if i - k == q[0]:
                q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            res.append(nums[q[0]])
        
        return res
    

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))
print(Solution().maxSlidingWindow([1000, 1, 999, 1, 5], 3))

