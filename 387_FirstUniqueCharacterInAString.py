from collections import defaultdict
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx_map = defaultdict(list)
        N = len(s)
        ans = N

        for i, c in enumerate(s):
            idx_map[c].append(i)

        for idxs in idx_map.values():
            if len(idxs) == 1:
                ans = min(ans, idxs[0])
        
        return -1 if ans == N else ans

    def firstUniqChar(self, s: str) -> int:
        cnt_map = Counter(s)

        for i, c  in enumerate(s):
            if cnt_map[c] == 1:
                return i
        return -1
    
print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))