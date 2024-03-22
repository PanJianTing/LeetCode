class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        N = len(s)
        cnt = 0

        for i in range(N):
            if s[i] == c:
                cnt += 1

        return (cnt * (cnt + 1)) >> 1
        return cnt + ((cnt * (cnt-1)) >> 1)
    
print(Solution().countSubstrings("abada", "a"))
print(Solution().countSubstrings("zzz", "z"))