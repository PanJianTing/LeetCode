
class Solution:
    def countHomogenous(self, s) -> int:
        s += "@"
        ans = 0
        cur = 1
        N = len(s)
        for i in range(1, N):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans += (((cur + 1) * cur) >> 1)
                cur = 1
        return ans % (10 ** 9 + 7)
    
    def countHomogenous(self, s) -> int:
        ans = 0
        cur = None
        cnt = 0

        for c in s:
            cnt = cnt + 1 if cur == c else 1            
            cur = c
            ans += cnt
        return ans % (10 ** 9 + 7)
    
    def countHomogenous(self, s) -> int:
        res = 0
        for c, s in groupby(s):
            cnt = len(list(s))
            res += ((cnt * (cnt + 1)) >> 1)

        return res
    
    def countHomogenous(self, s) -> int:
        res = 0
        pre = None
        cnt = 0
        for c in s:
            if c == pre:
                cnt += 1
            else:
                cnt = 1
            pre = c
            res += cnt

        return res % (10 ** 9 + 7)
    


print(Solution().countHomogenous("abbcccaa"))
print(Solution().countHomogenous("xy"))
print(Solution().countHomogenous("zzzzz"))