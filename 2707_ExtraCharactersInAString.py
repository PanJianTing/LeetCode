from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dictionary = set(dictionary)
        N = len(s)

        @cache
        def dp(idx):
            if idx == N:
                return 0
            
            ans = dp(idx+1) + 1
            for i in range(idx, N):
                cur = s[idx: i+1]
                if cur in dictionary:
                    ans = min(ans, dp(i+1))
            return ans

        return dp(0)
    
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        N = len(s)
        dictionary = set(dictionary)
        dp = [0] * (N+1)

        for st in range(N-1, -1, -1):
            dp[st] = dp[st+1] + 1
            for end in range(st, N):
                cur = s[st: end+1]

                if cur in dictionary:
                    dp[st] = min(dp[st], dp[end+1])
        
        return dp[0]

    
print(Solution().minExtraChar("leetscode", ["leet","code","leetcode"]))
print(Solution().minExtraChar("sayhelloworld", ["hello","world"]))
print(Solution().minExtraChar("dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))

