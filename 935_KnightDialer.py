from functools import cache

class Solution:
    def knightDialer(self, n: int) -> int:
        connect_map = {0: [4, 6], 
                       1: [6, 8], 
                       2: [7, 9], 
                       3: [4, 8], 
                       4: [0, 3, 9], 
                       5: [], 
                       6: [0, 1, 7], 
                       7: [2, 6], 
                       8: [1, 3], 
                       9: [2, 4], 
                       }
        
        @cache
        def dp(cur, cur_idx):
            if cur_idx == n:
                return 1
            
            temp = 0
            for num in connect_map[cur]:
                temp += dp(num, cur_idx+1)
            
            return temp
        ans = 0
        for i in range(10):
            ans += dp(i, 1)

        return ans % (10 ** 9 + 7)
    

    def knightDialer(self, n) -> int:
        mod = 10 ** 9 + 7
        connect_map = {0: [4, 6], 
                       1: [6, 8], 
                       2: [7, 9], 
                       3: [4, 8], 
                       4: [0, 3, 9], 
                       5: [], 
                       6: [0, 1, 7], 
                       7: [2, 6], 
                       8: [1, 3], 
                       9: [2, 4], 
                       }
        
        dp = [[0] * 10 for _ in range(n)]

        for i in range(10):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(10):
                ans = 0
                for next in connect_map[j]:
                    ans += (dp[i-1][next] % mod)
                
                dp[i][j] = ans % mod

        return sum(dp[n-1]) % mod
    

    def knightDialer(self, n) -> int:
        mod = 10 ** 9 + 7
        connect_map = {0: [4, 6], 
                       1: [6, 8], 
                       2: [7, 9], 
                       3: [4, 8], 
                       4: [0, 3, 9], 
                       5: [], 
                       6: [0, 1, 7], 
                       7: [2, 6], 
                       8: [1, 3], 
                       9: [2, 4], 
                       }
        
        dp = [1] * 10

        for _ in range(1, n):
            next_dp = [0] * 10
            for j in range(10):
                ans = 0
                for next in connect_map[j]:
                    ans += (dp[next] % mod)
                
                next_dp[j] = ans
            dp = next_dp

        return sum(dp) % mod
    

# print(Solution().knightDialer(1))
# print(Solution().knightDialer(2))
# print(Solution().knightDialer(3))
# print(Solution().knightDialer(4))
print(Solution().knightDialer(3131))
