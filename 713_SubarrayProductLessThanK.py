import math

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0

        for cnt in range(1, N+1):
            for st in range(N):
                end = st + cnt
                if end > N:
                    continue
                all_product = 1
                for i in range(st, end):
                    all_product *= nums[i]
                
                if all_product < k:
                    res += 1
        return res
    
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0
        l = 0
        r = 0
        cur = 1

        while r < N:
            cur *= nums[r]
            while l < r and cur >= k:
                cur //= nums[l]
                l += 1
            
            if cur < k:
                res += (r-l)+1
            r += 1
        return res
    

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0
        logK = math.log(k)
        N = len(nums)
        M = N+1
        logPrefixSum = [0] * M
        res = 0

        for i in range(1, M):
            logPrefixSum[i] = math.log(nums[i-1]) + logPrefixSum[i-1]

        for i in range(M):
            l = i+1
            r = M-1
            while l <= r:
                mid = l + ((r-l) >> 1)
                if logPrefixSum[mid] < (logPrefixSum[i] + logK - 1e-9):
                    l = mid + 1
                else:
                    r = mid - 1
            res += l - i - 1

        return res
            
            

    
print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))
print(Solution().numSubarrayProductLessThanK([1,2,3,4], 0))
print(Solution().numSubarrayProductLessThanK([1,2,3,4,5], 1))