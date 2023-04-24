class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []

        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)

        return "".join(ans)
    

    def removeDuplicates(self, s: str) -> str:
        i = 0
        s = list(s)
        n = len(s)
        for j in range(0, n):
            s[i] = s[j]
            if i > 0 and s[i-1] == s[i]:
                i -= 2
            i += 1
        return "".join(s[0:i])
