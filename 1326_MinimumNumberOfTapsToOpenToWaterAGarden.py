class Solution:
    
    def minTaps(self, n, ranges):
        k = 1000000000
        dp = [k] * (n+1)

        dp[0] = 0

        for i, r in enumerate(ranges):
            tap_st = max(0, i - r)
            tap_en = min(n, i + r)

            for j in range(tap_st, tap_en+1):
                dp[tap_en] = min(dp[tap_en], dp[j]+1)
        
        if dp[n] == k:
            dp[n] = -1
        return dp[n]
    
    def minTaps(self, n, ranges):
        max_reach = [0] * (n+1)
        for i, r in enumerate(ranges):
            start = max(0, i-r)
            end = min(n, i+r)

            max_reach[start] = max(max_reach[start], end)

        cur_end = 0
        next_end = 0
        tap = 0
        
        for i in range(n+1):
            if i > next_end:
                return -1
            
            if i > cur_end:
                tap += 1
                cur_end = next_end
            
            next_end = max(next_end, max_reach[i])
        
        return tap




print(Solution().minTaps(9, [0,5,0,3,3,3,1,4,0,4]))
print(Solution().minTaps(5, [3,4,1,1,0,0]))
print(Solution().minTaps(3, [0,0,0,0]))
print(Solution().minTaps(7, [1,2,1,0,2,1,0,1]))
print(Solution().minTaps(8, [4,0,0,0,4,0,0,0,4]))
