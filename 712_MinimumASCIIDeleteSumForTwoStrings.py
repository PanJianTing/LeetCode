class Solution:

    # 此方法無解，因為如果相等的話，必須要比對前面的順序，故要多一個空字串來當base case。
    def minimumDeleteSum(self, s1, s2) -> int:
        M = len(s1)
        N = len(s2)

        dp = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if s1[i] == s2[j]:
                    if i == 0 and j == 0:
                        dp[i][j] = 0
                    else:
                        if i == 0:
                            dp[i][j] = dp[i][j-1] - ord(s2[j])
                        elif j == 0:
                            dp[i][j] = dp[i-1][j] - ord(s1[i])
                        else:
                            dp[i][j] = dp[i-1][j-1]

                else:
                    if i == 0 and j == 0:
                        dp[i][j] = ord(s1[i]) + ord(s2[j])
                    else:
                        if i == 0:
                            dp[i][j] = dp[i][j-1] + ord(s2[j])
                        elif j == 0:
                            dp[i][j] = dp[i-1][j] + ord(s1[i])
                        else:
                            dp[i][j] = min(dp[i][j-1] + ord(s2[j]), dp[i-1][j] + ord(s1[i]))

        print(dp)

        return dp[M-1][N-1]
    

    def minimumDeleteSum(self, s1, s2) -> int:
        M = len(s1)
        N = len(s2)

        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(1, M+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for i in range(1, N+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        
        for i in range(1, M+1):
            for j in range(1, N+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[M][N]
    
    # time > O(3^K * K), space > O(n)
    def minimumDeleteSum(self, s1, s2) -> int:

        def computeCost(i, j) -> int:

            if i < 0:
                temp = 0
                for idx in range(0, j+1):
                    temp += ord(s2[idx])
                return temp
            
            if j < 0:
                temp = 0
                for idx in range(0, i+1):
                    temp += ord(s1[idx])
                return temp
            
            if s1[i] == s2[j]:
                return computeCost(i-1, j-1)
            else:
                return min(ord(s1[i]) + computeCost(i-1, j), ord(s2[j]) + computeCost(i, j-1), ord(s1[i]) + ord(s2[j]) + computeCost(i-1, j-1))
            
        return computeCost(len(s1)-1, len(s2)-1)
    
    # Time > O(M * N), Space > O(M * N)
    def minimumDeleteSum(self, s1, s2) -> int:

        M = len(s1)
        N = len(s2)

        result = {}

        def computeCost(i, j) -> int:
            if i < 0 and j < 0:
                return 0
            
            if (i, j) in result:
                return result[(i, j)]

            if i < 0:
                result[(i, j)] = ord(s2[j]) + computeCost(i, j-1)
                return result[(i, j)]
            
            if j < 0:
                result[(i, j)] = ord(s1[i]) + computeCost(i-1, j)
                return result[(i, j)]
            
            if s1[i] == s2[j]:
                result[(i, j)] = computeCost(i-1, j-1)
            else:
                result[(i, j)] = min(ord(s1[i]) + computeCost(i-1, j), ord(s2[j]) + computeCost(i, j-1))

            return result[(i, j)]
        
        computeCost(len(s1) - 1, len(s2) - 1)
        return result[(M-1, N-1)]
            



print(Solution().minimumDeleteSum("sea", "eat"))            # 231
print(Solution().minimumDeleteSum("delete", "leet"))        # 403
print(Solution().minimumDeleteSum("sjfqkf", "fxymelgo"))    # 1316

