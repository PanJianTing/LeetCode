from collections import defaultdict

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n+1)]

        for i in range(0, n):
            for j in range(0, n):
                dp[1][i][j] = s1[i] == s2[j]

        for length in range(2, n+1):
            for i in range(0, n+1-length):
                for j in range(0, n+1-length):
                    for newL in range(1, length):
                        dp1 = dp[newL][i]
                        dp2 = dp[length - newL][i + newL]

                        dp[length][i][j] |= dp1[j] and dp2[j+newL]
                        dp[length][i][j] |= dp1[j+length - newL] and dp2[j]


        return dp[n][0][0]
    
    def isHelper(self, s1: str, s2: str, cache: dict) -> bool:
        print(s1, s2)

        key = (s1, s2)
        key_r = (s2, s1)
        if key in cache:
            return cache[key]
        if key_r in cache:
            return cache[key_r]
        
        n = len(s1)

        if sorted(s1) != sorted(s2):
            cache[key] = False
            return False
        if n <= 3:
            cache[key] = True
            return True
        
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        count_s2_r = defaultdict(int)

        for i in range(1, n):

            count_s1[s1[i-1]] += 1
            count_s2[s2[i-1]] += 1
            count_s2_r[s2[-i]] += 1

            if count_s1 == count_s2:
                cache[key] = self.isHelper(s1[0:i], s2[0:i], cache) and self.isHelper(s1[i:n], s2[i:n], cache)
                if cache[key]:
                    return True
            if count_s1 == count_s2_r:
                cache[key] = self.isHelper(s1[0:i], s2[n-i:n], cache) and self.isHelper(s1[i:n], s2[0:n-i], cache)
                if cache[key]:
                    return True
        return False


    # def isScramble(self, s1: str, s2: str) -> bool:
    #     cache = dict()
    #     return self.isHelper(s1, s2, cache)

Solution().isScramble("great", "rgeat")

# Solution().isScramble("abcde", "caebd")
