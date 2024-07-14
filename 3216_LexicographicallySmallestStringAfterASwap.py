class Solution:
    def getSmallestString(self, s: str) -> str:
        N = len(s)
        s = list(s)
        

        for i in range(1, N):
            pre_c = int(s[i-1])
            cur_c = int(s[i])

            if (pre_c & 1 == cur_c & 1) and pre_c > cur_c:
                s[i-1], s[i] = s[i], s[i-1]
                break
        return ''.join(s)

print(Solution().getSmallestString('45320'))
print(Solution().getSmallestString('001'))
