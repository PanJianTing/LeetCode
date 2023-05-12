class Solution:
    memo = []
    def dp(self, i: int, q: list[list[int]]) -> int:

        if (i < len(q)) == False:
            return 0
        
        if self.memo[i] != -1:
            return self.memo[i]
        
        point = q[i][0]
        skip = q[i][1]

        self.memo[i] = max(point + self.dp(i+skip+1, q), self.dp(i+1, q))
        return self.memo[i]
    
    def mostPoints(self, q: list[list[int]]) -> int:
        self.memo = [-1] * len(q) 
        return self.dp(0, q)
    
    def mostPoints(self, q: list[list[int]]) -> int:
        n = len(q)
        dp = [-1] * n

        for i in range(n-1, -1, -1):
            point = q[i][0]
            skip = q[i][1]
            if i + 1 >= n:
                dp[i] = point
            else:
                if i + 1 + skip >= n:
                    dp[i] = max(point, dp[i+1])
                else:
                    dp[i] = max(point + dp[i+1+skip], dp[i+1])
                
        return dp[0]
    
    def mostPoints(self, q: list[list[int]]) -> int:
        n = len(q)
        dp = [-1] * n
        dp[-1] = q[-1][0]

        for i in range(n-2, -1, -1):
            dp[i] = q[i][0]
            skip = q[i][1]
            if i + 1 + skip < n:
                dp[i] += dp[i+1+skip]
            dp[i] = max(dp[i], dp[i+1])

        return dp[0]
    

print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))


