from functools import lru_cache
from functools import cache
from math import gcd


class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def backtrack(self, nums: list[int], mask: int, pairPick: int, memo: list[int]) -> int:

        if pairPick << 1 == len(nums):
            return 0
        
        if memo[mask] != -1:
            return memo[mask]

        sc = 0

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if ((mask >> i) & 1) == 1 or ((mask >> j) & 1) == 1:
                    continue
                newMask = mask | (1 << i) | (1 << j)

                currSc = (pairPick + 1) * self.gcd(nums[i], nums[j])
                remainingSc = self.backtrack(nums, newMask, pairPick + 1, memo)

                sc = max(sc, currSc + remainingSc)

        memo[mask] = sc
        return sc

    def maxScore(self, nums: list[int]) -> int:
        size = 1 << len(nums) # 2^n
        memo = [-1] * size
        return self.backtrack(nums, 0, 0, memo)
    
    def maxScore(self, nums: list[int]) -> int:
        maxState = 1 << len(nums)
        finalMask = maxState - 1

        dp = [-1] * maxState

        for state in range(finalMask, -1, -1):
            if state == finalMask:
                dp[state] = 0
                continue
            numberTaken = bin(state).count('1')
            pairFormed = numberTaken >> 1
            if numberTaken % 2:
                continue

            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    

                    if (state >> i) & 1 == 1 or (state >> j) & 1 == 1:
                        continue

                    curr = (pairFormed + 1) * self.gcd(nums[i], nums[j])
                    other = state | (1 << i) | (1 << j)
                    dp[state] = max(dp[state], curr + dp[other])
        print(dp)
        return dp[0]
    
    def maxScore(self, n: list[int]) -> int:

        @lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i > (len(n) >> 1):
                return 0
            res = 0
            for j in range(len(n)):
                for k in range(j+1, len(n)):
                    new = (1 << j) + (1 << k)
                    if not mask & new:
                        res = max(res, i * gcd(n[j], n[k])+ dfs(i+1, mask + new))

            return res
        return dfs(1, 0)
    
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums) >> 1

        @cache
        def dp(i, mask) -> tuple:
            if i == 1 << n:
                return ([])
            if not (mask >> i) & 1:
                return dp(i+1, mask)    
            ans = []
            tot = 0
            mask -= (1 << i)
            for j in range(i+1, n << 1):
                if (mask >> j) & 1:
                    gcds = sorted(dp(i+1, mask - (1 << j)) + [gcd(nums[i], nums[j])])
                    sc = sum((i + 1) * gcds[i] for i in range(len(gcds)))
                    if sc > tot:
                        ans = gcds
                        tot = sc
            return ans
        gcds = sorted(dp(0, (1 << (1 << n))-1))
        return sum((i + 1) * gcds[i] for i in range(n))

            

        

print(Solution().maxScore([3,4,6,8]))


