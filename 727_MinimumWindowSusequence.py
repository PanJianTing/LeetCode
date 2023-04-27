class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)

        dp = [[0 for _ in range(0, m)] for _ in range(0, n)]

        for j, c2 in enumerate(s2):
            for i, c1 in enumerate(s1):
                if c1 == c2:
                    dp[j][i] = 1

        ans = s1
        j = 0
        start = -1
        end = 0
        haveAns = False
        for i in range(m):
            if dp[j][i]:
                j += 1
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
                
                if j == n:
                    temp = s1[start:end+1]
                    haveAns = True
                    if len(ans) > len(temp):
                        ans = temp
                    j = 0
                    start = -1

        return ans if haveAns else ""
    

print(Solution().minWindow("abcdebdde", "bde"))
print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))
print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "k"))
