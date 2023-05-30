from functools import cache

'''
dp[i, m] = maximum stones the current player can get from piles[i:] with M=m
A[i]= total stones of piles[i:]
when current player pick stones from i to i+x-1
-> the other player's stones: dp[i+x, max(m, x)]
-> total stones of current player: A[i] - dp[i+x, max(m, x)]
we want the current player gets maximum means the other player gets minimum
'''

class Solution:
    def stoneGameII(self, A: list[int]) -> int:
        
        @cache
        def f(p, i, m) -> int:
            if i == len(A):
                return 0
            res = 1000000 if p == 1 else -1
            s = 0
            
            for x in range(1, min(2 * m, len(A) - i) + 1):
                s += A[i + x - 1]
                if p == 0:
                    res = max(res, s + f(1, i+x, max(m, x)))
                else:
                    res = min(res, f(0, i + x, max(m, x)))

            return res
        return f(0, 0, 1)
    
    def stoneGameII(self, A: list[int]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            print(i)
            A[i] += A[i+1]
        
        @cache
        def dp(i, m):
            print(i, m)
            if i + 2 * m >= N: return A[i]
            # 減掉對手拿最少數量的。
            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2*m+1))
        
        return dp(0, 1)


# print(Solution().stoneGameII([2, 7, 9, 4, 4]))
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))