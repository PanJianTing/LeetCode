class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        pre_c = ""
        cur_cnt = 0

        for c in s:
            if pre_c == c:
                cur_cnt += 1
            else:
                pre_c = c
                cur_cnt = 1
            
            if cur_cnt < 3:
                ans.append(c)

        return "".join(ans)
    

    def makeFancyString(self, s: str) -> str:
        N = len(s)
        if N < 3:
            return s

        left = 2
        s = list(s)

        for right in range(2, N):
            if (s[right] != s[left-1] or s[right] != s[left-2]):
                s[left] = s[right]
                left += 1
        
        return "".join(s[:left])
    
# print(Solution().makeFancyString("leeetcode"))
print(Solution().makeFancyString("aaabaaaa"))
print(Solution().makeFancyString("aab"))