from functools import cache

class Solution:
    # dp
    def minOperations(self, nums: list[int], x: int) -> int:
        l = 0
        r = len(nums) - 1
        inf = float("inf")
        
        @cache
        def dp(left, right, curr):

            if curr == 0:
                return 0
            
            if left > right or curr < 0:
                return inf
            

            return 1 + min(dp(left+1, right, curr - nums[left]), dp(left, right-1, curr - nums[right]))
            

        ans = dp(l, r, x)
        return -1 if inf == ans else ans
    
    def minOperations(self, nums, x):

        N = len(nums)
        total = sum(nums)
        find = total - x

        # set -1, because maybe sum(nums) == x
        maxCnt = -1
        # from 0, becasue you maybe minus first element
        l = 0
        cur = 0

        for r in range(0, N):
            cur += nums[r]
            while cur > find and l <= r:
                cur -= nums[l]
                l += 1
            if cur == find:
                maxCnt = max(maxCnt, r-l+1)
            

        return -1 if maxCnt == -1 else N - maxCnt
    
    def minOperations(self, nums, x):
        N = len(nums)
        total = sum(nums)
        ans = float('inf')

        l = 0
        for r in range(N):
            total -= nums[r]
            while total < x and l <= r:
                total += nums[l]
                l += 1
            
            if total == x:
                ans = min(ans, N - r + l - 1)
        
        return -1 if ans == float('inf') else ans


# print(Solution().minOperations([10,1,1,1,1,1], 5))
print(Solution().minOperations([1,1,4,2,3], 5))
print(Solution().minOperations([5,6,7,8,9], 4))
print(Solution().minOperations([3,2,20,1,1,3], 10))
# print(Solution().minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))