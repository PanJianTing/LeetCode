from functools import cache

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k) -> int:
        N = len(arr)

        @cache
        def dp(idx) -> int:
            if idx == N:
                return 0
            res = 0
            cur_max = 0
            for i in range(idx, min(idx+k, N)):
                cur_max = max(cur_max, arr[i])
                res = max(res, cur_max * (i-idx+1) + dp(i+1))
            return res
        
        return dp(0)
    
    def maxSumAfterPartitioning(self, arr: list[int], k) -> int:
        N = len(arr)
        dp = [0] * (N+1)
    
        for i in range(N-1, -1, -1):
            cur_max = 0
            for j in range(i, min(i+k, N)):
                cur_max = max(cur_max, arr[j])
                dp[i] = max(dp[i], cur_max * (j-i+1) + dp[j+1])
        print(dp)
        return dp[0]
    

    def maxSumAfterPartitioning(self, arr: list[int], k) -> int:
        N = len(arr)
        K = k+1
        dp = [0] * (K)

        for i in range(N-1, -1, -1):
            cur_max = 0
            for j in range(i, min(i+k, N)):
                print(i, j, (j+1) % K)
                cur_max = max(cur_max, arr[j])
                dp[i%K] = max(dp[i%K], cur_max * (j-i+1) + dp[(j+1) % K])

        return dp[0]

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        N = len(arr)
        dp_length = k+1
        dp = [0] * dp_length
        

        for i in range(N-1, -1, -1):
            cur_max = 0
            for j in range(i, min(i+k, N)):
                cur_max = max(cur_max, arr[j])
                dp[i%dp_length] = max(dp[i%dp_length], cur_max * (j-i+1) + dp[(j+1) % (dp_length)])

        return dp[0]

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))