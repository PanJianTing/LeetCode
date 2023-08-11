from functools import cache
class Solution:
    def change(self, amount, coins) -> int:
        N = len(coins)

        def find(a):
            if a == 0:
                return 1
            
            if a < 0:
                return 0
            ans = 0
            for coin in coins:
                ans += find(a-coin)
            return ans

        return find(amount)
    
    def achange(self, amount, coins) -> int:
        N = len(coins)
        
        @cache
        def search(i, a):
            if i == N:
                return 0
            if a == 0:
                return 1

            if coins[i] > a:
                return search(i+1, a)
            
            return search(i+1, a) + search(i, a-coins[i])
        
        return search(0, amount)
    
    def change(self, amount, coins) -> int:

        N = len(coins)
        dp = [[0] * (N+1) for _ in range(amount+1)]
        dp[0][0] = 1

        for i in range(N+1):
            dp[0][i] = 1

        for a in range(1, amount+1):
            for i in range(0, N):
                if coins[i] > a:
                    dp[a][i+1] = dp[a][i]
                else:
                    dp[a][i+1] = dp[a][i] + dp[a-coins[i]][i+1]
        
        return dp[amount][N]
    
    def change(self, amount, coins) -> int:
        N = len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]

        for i in range(0, (N+1)):
            dp[i][0] = 1
        
        for i in range(0, N):
            for a in range(1, amount+1):
                if coins[i] > a:
                    dp[i+1][a] = dp[i][a]
                else:
                    dp[i+1][a] = dp[i][a] + dp[i+1][a-coins[i]]

        return dp[N][amount]
    
    def change(self, amount, coins) -> int:
        N = len(coins)
        dp = [0] * (amount + 1)

        dp[0] = 1
        newDp = dp[:]

        for i in range(0, N):
            newDp[0] = 1
            for a in range(1, amount+1):
                if coins[i] > a:
                    newDp[a] = dp[a]
                else:
                    newDp[a] = dp[a] + newDp[a-coins[i]]
            dp = newDp[:]
            
        return dp[amount]
    
    def change(self, amount, coins) -> int:
        N = len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]

        for i in range(N):
            dp[i][0] = 1
        
        for i in range(N-1, -1, -1):
            for a in range(1, amount+1):
                if coins[i] > a:
                    dp[i][a] = dp[i+1][a]
                else:
                    dp[i][a] = dp[i+1][a] + dp[i][a - coins[i]]

        return dp[0][amount]
    
    def change(self, amount, coins) -> int:
        N = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(0, N):
            for a in range(coins[i], amount+1):
                # if coins[i] <= a:
                dp[a] += dp[a-coins[i]]
                    
        return dp[amount]




print(Solution().change(5, [1,2,5]))    # 4
print(Solution().change(6, [2,2,1]))    # 10

