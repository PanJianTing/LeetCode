class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, maxPts+1):
                print(i, j)
                if i-j >= 0 and i-j < k:
                    print(f"add {i-j}")
                    dp[i] += dp[i-j] / maxPts
            print(dp)

        print(dp) 
        return sum(dp[k:])
    

    def new21Game(self, n, k, maxPts) -> float:
        dp = [0] * (n+1)
        dp[0] = 1
        s = 1 if k > 0 else 0

        for i in range(1, n+1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i-maxPts]

        return sum(dp[k:])

    def new21Game(self, N, K, W):
        if K == 0 or N >= K+W: return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0

        for i in range(1, N+1):
            dp[i] = Wsum / W
            if i < K: Wsum += dp[i]
            if i - W >= 0: Wsum -= dp[i-W]
        return sum(dp[K:])  
    

# print(Solution().new21Game(10, 1, 10))
print(Solution().new21Game(21, 17, 10))