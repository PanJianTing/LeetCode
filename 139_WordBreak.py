from collections import defaultdict, deque
from functools import cache


class Solution:
    def wordBreak(self, s, wordDict) -> bool:

        if s == "":
            return True
        
        words = defaultdict(list)

        for word in wordDict:
            words[word[0]].append(word)


        @cache
        def dp(s) -> bool:
            if s == "":
                return True
        
            now = s[0]
            if now not in words:
                return False
            
            ans = False
            for w in words[now]:
                l = 0
                leng = len(w)
                while l < len(s):
                    check = s[l:l+leng]
                    if check == w:
                        l += leng
                    else:
                        break
                ans |= dp(s[l:])

                # check = s[0:l]
                # if check == w:
                #     ans |= self.dp(s[l:], words)
            return ans
        
        return dp(s)
    
    def wordBreak(self, s, wordDict) -> bool:

        @cache
        def dp(i) -> bool:
            if i < 0:
                return True
            
            ans = False
            for w in wordDict:
                l = len(w)
                check = s[i-l+1 : i+1]
                ans |= (check == w and dp(i-l))
            return ans
        
        return dp(len(s) - 1)
    

    def wordBreak(self, s, wordDict) -> bool:

        @cache
        def dp(i) -> bool:
            if i < 0:
                return True
            
            for w in wordDict:
                l = len(w)
                check = s[i-l+1 : i+1]

                if check == w and dp(i-l):
                    return True
            return False
        
        return dp(len(s) - 1)
    
    def wordBreak(self, s, wordDict) -> bool:

        N = len(s)
        q = deque()
        seen = [False] * (N+1)
        
        q.append(0)
        seen[0] = True

        while q:
            curr = q.popleft()
            if curr == N:
                return True
            for end in range(curr+1, N+1):
                if seen[end]:
                    continue

                check = s[curr:end]
                if check in wordDict:
                    q.append(end)
                    seen[end] = True
        return False
    
    def wordBreak(self, s, wordDict) -> bool:
        N = len(s)
        dp = [False] * N

        for i in range(0, N):
            for w in wordDict:
                l = len(w)
                if (i - l + 1) < 0:
                    continue

                if i == l - 1 or dp[i - l]:
                    check = s[i-l+1: i+1]
                    if check == w:
                        dp[i] = True
                        break
        return dp[N-1]
    
    def wordBreak(self, s, wordDict) -> bool:
        N = len(s)
        dp = [False] * N

        for i in range(N):
            for w in wordDict:
                l = len(w)
                
                if i+1 == l or (i - l >= 0 and dp[i-l]):
                    check = s[i-l+1: i+1]
                    if check == w:
                        dp[i] = True
                        break
        return dp[N-1]

            


    

print(Solution().wordBreak("a", ["aa","aaa","aaaa","aaaaa","aaaaaa"]))          # False
print(Solution().wordBreak("leetcode", ["leet","code"]))                        # True
print(Solution().wordBreak("applepenapple", ["apple","pen"]))                   # True
print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))     # False
print(Solution().wordBreak("cars", ["car","ca","rs"]))                          # True
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
                           ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])) # False
        
        
        
