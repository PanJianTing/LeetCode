class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        cnt = 0

        def isPalindrom(i, j) -> bool:

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for i in range(N):
            for j in range(i, N):
                if isPalindrom(i, j):
                    cnt += 1
        return cnt
    
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        dp = [[False] * N for _ in range(N)]

        for l in range(1, N+1):
            for i in range(N):
                j = i+(l-1)
                if j >= N:
                    continue
                if i == j:
                    dp[i][j] = True
                elif j-i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) & dp[i+1][j-1]
                
                ans += dp[i][j]
        return ans
    
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        def countPalindroms(i, j) -> int:
            cnt = 0
            while i >= 0 and j < N:
                if s[i] == s[j]:
                    cnt += 1
                else:
                    break
                i -= 1
                j += 1
            return cnt
        
        for i in range(N):
            # odd length
            ans += countPalindroms(i, i)

            # even length
            ans += countPalindroms(i, i+1)
            
        return ans


            


print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))
print(Solution().countSubstrings("aba"))
print(Solution().countSubstrings("aaaaa"))