class Solution:
    def maxA(self, n: int) -> int:

        dp = [0 for _ in range(n+1)]

        for i in range(0, n+1):
            dp[i] = i

        for i in range(0, n-2):
            for j in range(i+3, min(n, i+6)+1):
                print(i, j)
                dp[j] = max(dp[j], (j-i-1) * dp[i])
        return dp[n]

class Solution:
    def maxA(self, n: int) -> int:
        mx = [1,2,3,4,5]
        if n <= 5:
            return mx[n-1]
        
        for i in range(5, n):
            mx.append(max(mx[-3]*2, mx[-4]*3, mx[-5]*4))

        return mx[n-1]

Solution().maxA(7)

        

        