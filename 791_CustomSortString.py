from collections import defaultdict
from functools import cmp_to_key

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt_map = defaultdict(int)
        res = ''

        for c in s:
            cnt_map[c] += 1
        
        for c in order:
            res += c * cnt_map[c]
            cnt_map[c] = 0
        
        for c in cnt_map:
            res += c * cnt_map[c]
        
        return res

    def customSortString(self, order: str, s: str) -> str:
        cnt_map = defaultdict(int)
        res = []

        for c in s:
            cnt_map[c] += 1
        
        for c in order:
            res.append(c * cnt_map[c])
            cnt_map[c] = 0
        
        for c in cnt_map:
            res.append(c * cnt_map[c])
        
        return "".join(res)
    
    def customSortString(self, order: str, s: str) -> str:

        idx_map = defaultdict(lambda: 27)
        
        for idx, c in enumerate(order):
            idx_map[c] = idx

        s = sorted(s, key=lambda x: idx_map[x])

        return ''.join(s)
        
    
print(Solution().customSortString('cba', 'abcd'))
print(Solution().customSortString('bcafg', 'abcd'))

        