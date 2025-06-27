from collections import deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        N = len(s)
        q = deque()
        q.append("")
        ans = ""

        def isK(cur_s):
            cnt = 0
            i = 0
            for c in s:
                if i < len(cur_s) and c == cur_s[i]:
                    i += 1
                    if i == len(cur_s):
                        i = 0
                        cnt += 1
                        if cnt == k:
                            return True
            return False

        while q:
            cur_chr = q.popleft()
            for c in range(26):
                new_chr = cur_chr + chr(ord('a') + c)
                if isK(new_chr):
                    if len(new_chr) >= len(ans):
                        ans = new_chr
                    q.append(new_chr)
        return ans
    

print(Solution().longestSubsequenceRepeatedK("letsleetcode", 2))