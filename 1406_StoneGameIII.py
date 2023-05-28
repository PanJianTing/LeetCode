from functools import cache


def cmp(a, b):
        return (a>b) - (a<b)
class Solution:

    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        for i in range(N-2, -1, -1):
            A[i] += A[i+1]

        maxStone = A[0]
        
        @cache
        def dp(idx):
            if idx >= N:
                return 0
            A[idx] -= min(dp(idx + i) for i in range(1, 3+1))
            return A[idx]
            
            
        cnt = dp(0)
        
        if maxStone - cnt > cnt:
            return 'Bob'
        elif maxStone - cnt < cnt:
            return 'Alice'

        return 'Tie'
    
    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        dp = [0] * (N + 1)

        for i in range(N-1, -1, -1):
            dp[i] = A[i] - dp[i+1]
            
            if i + 2 <= N:
                dp[i] = max(dp[i], A[i] + A[i+1] - dp[i+2])
            if i+3 <= N:
                dp[i] = max(dp[i], A[i] + A[i+1] + A[i+2] - dp[i+3])
        
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return 'Bob'
        return "Tie"
    
    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        
        @cache
        def dp(i):
            if i >= N:
                return 0
            result = A[i] - dp(i+1)
            if i + 2 <= N:
                result = max(result, A[i] + A[i+1] - dp(i+2))
            if i+3 <= N:
                result = max(result, A[i] + A[i+1] + A[i+2] - dp(i+3))

            return result
        diff = dp(0)

        if diff > 0:
            return 'Alice'
        if diff < 0:
            return 'Bob'
        return 'Tie'
    
    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        dp = [0] * 4
        for i in range(N-1, -1, -1):
            dp[i % 4] = A[i] - dp[(i+1) % 4]

            if i + 2 <= N:
                dp[i % 4] = max(dp[i % 4], A[i] + A[i+1] - dp[(i+2) % 4])

            if i+3 <= N:
                dp[i % 4] = max(dp[i % 4], A[i] + A[i+1] + A[i+2] - dp[(i+3) % 4])

        if dp[0] > 0:
            return 'Alice'
        if dp[0] < 0:
            return 'Bob'
        return 'Tie'
    
    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        dp = [0] * (N+1)

        for i in range(N-1, -1, -1):
            dp[i] = -999999999
            take = 0
            for k in (0, 1, 2):
                if i+k < N:
                    take += A[i+k]
                    dp[i] = max(dp[i], take - dp[i+k+1])
        
        if dp[0] > 0: return 'Alice'
        if dp[0] < 0: return 'Bob'
        return 'Tie' 

    def stoneGameIII(self, A: list[int]) -> str:
        N = len(A)
        dp = [0] * 3

        for i in range(N-1, -1, -1):
            dp[i % 3] = max(sum(A[i: i+k]) - dp[(i+k) % 3] for k in (1, 2, 3))
        
        return ['Tie', 'Alice', 'Bob'][cmp(dp[0], 0)]

            

print(Solution().stoneGameIII([1,2,3,7]))