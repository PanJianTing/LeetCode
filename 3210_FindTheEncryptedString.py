from collections import defaultdict
import heapq

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        N = len(s)
        res = ''
        for i, c in enumerate(s):
            next_idx = (i + k) % N
            res += s[next_idx]
        return res
            
    def getEncryptedString(self, s: str, k: int) -> str:
        N = len(s)
        res = [''] * N

        for i in range(N):
            next_idx = (i + k) % N
            res[i] = s[next_idx]
        return ''.join(res)
    

print(Solution().getEncryptedString('dart', 3))
print(Solution().getEncryptedString('aaa', 1))