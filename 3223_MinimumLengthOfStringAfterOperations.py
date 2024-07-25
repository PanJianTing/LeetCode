from collections import defaultdict, Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt_map = defaultdict(int)
        res = 0

        for c in s:
            cnt_map[c] += 1
        
        for k in cnt_map.keys():
            while cnt_map[k] > 2:
                cnt_map[k] -= 2
            res += cnt_map[k]
        return res
    

    def minimumLength(self, s: str) -> int:
        cnt_map = defaultdict(int)
        res = 0

        for c in s:
            cnt_map[c] += 1
        
        for k in cnt_map.keys():
            if cnt_map[k] & 1:
                res += 1
            else:
                if cnt_map[k] > 0:
                    res += 2
        return res
    
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        
        for c in cnt.values():
            if c & 1:
                res += 1
            else:
                res += (2 if c else 0)
        return res

print(Solution().minimumLength('abaacbcbb'))
print(Solution().minimumLength('aa'))

        