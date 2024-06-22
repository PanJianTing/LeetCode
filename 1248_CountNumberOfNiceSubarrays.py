from collections import defaultdict
from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: list[int], need_cnt: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            for j in range(i+1, N+1):
                odd_cnt = 0
                for k in range(i, j):
                    if nums[k] & 1:
                        odd_cnt += 1
                if odd_cnt == need_cnt:
                    print(nums[i:j])
                    res += 1
        return res
    
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0
        cur_sum = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        for i in range(N):
            cur_sum += (nums[i] & 1)
            if cur_sum - k in prefixSum:
                res += prefixSum[cur_sum-k]
            prefixSum[cur_sum] += 1
        return res
                
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0
        last = -1
        q = deque()

        for i in range(N):
            if nums[i] & 1:
                q.append(i)
            
            if len(q) > k:
                last = q.popleft()
            
            if len(q) == k:
                res += q[0] - last
        return res
    
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0
        st = 0
        cur_k = 0
        gap = 0

        for i in range(N):
            if nums[i] & 1:
                cur_k += 1
            if cur_k == k:
                gap = 0
                while cur_k == k:
                    cur_k -= (nums[st] & 1)
                    gap += 1
                    st += 1
            res += gap
        return res
    
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)

        def atMost(cur_k):
            st = 0
            res = 0
            cur_cnt = 0

            for i in range(N):
                cur_cnt += (nums[i] & 1)

                while cur_cnt > cur_k:
                    cur_cnt -= (nums[st] & 1)
                    st += 1
                res += (i - st + 1)
            
            return res
        return atMost(k) - atMost(k-1)

    
print(Solution().numberOfSubarrays([1,1,2,1,1], 1))
print(Solution().numberOfSubarrays([1,1,2,1,1], 3))
print(Solution().numberOfSubarrays([2,4,6], 1))
print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
