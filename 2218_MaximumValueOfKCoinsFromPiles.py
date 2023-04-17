from functools import lru_cache

class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        n = len(piles)

        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        # print(dp)

        for i in range(1,n+1):
            for coins in range(k+1):
                curr = 0
                for currCoins in range(min(len(piles[i-1]), coins) + 1):
                    print(i, coins, currCoins, curr)
                    if currCoins > 0:
                        curr += piles[i-1][currCoins-1]
                    dp[i][coins] = max(dp[i][coins], dp[i-1][coins - currCoins] + curr)
                print("=====")

        print(dp)

        return dp[n][k]
    
    piles = []
    @lru_cache(None)
    def f(self, i: int, coins: int) -> int:
        if i == 0:
            return 0
        
        curr = 0
        res = 0
        for currCoins in range(min(len(self.piles[i-1]), coins) + 1):
            if currCoins > 0:
                curr += self.piles[i-1][currCoins-1]
            res = max(res, self.f(i-1, coins-currCoins) + curr)

        return res


    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        n = len(piles)
        self.piles = piles



        return self.f(n, k)
    
    # top-down
    def maxValueOfCoins(self, A: list[list[int]], k: int) -> int:

        @lru_cache(None)
        def dp(i: int, k: int) -> int:
            if k == 0 or i == len(A):
                return 0
            
            res = dp(i+1, k)
            curr = 0
            for j in range(min(len(A[i]), k)):
                curr += A[i][j]
                res = max(res, curr + dp(i+1, k-j-1))
            return res

        return dp(0, k)
    
    # bottom-up
    def maxValueOfCoins(self, A: list[list[int]], k: int) -> int:

        n = len(A)

        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for pickCoins in range(0, k+1):
                curr = 0
                for j in range(min(len(A[i-1]), pickCoins)+1):
                    if j > 0:
                        curr += A[i-1][j-1]
                    dp[i][pickCoins] = max(dp[i][pickCoins], dp[i-1][pickCoins - j] + curr)


        return dp[n][k]






print(Solution().maxValueOfCoins([[1,100,3],[7,8,9]], 2))