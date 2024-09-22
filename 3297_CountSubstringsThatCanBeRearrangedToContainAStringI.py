from collections import defaultdict

class Solution:
    def validSubstringCount(self, w1: str, w2: str) -> int:
        M = len(w1)
        N = len(w2)

        if N > M:
            return 0
        
        w1_map = defaultdict(int)
        w2_map = defaultdict(int)

        for w in w2:
            w2_map[w] += 1
        
        res = 0
        requir = len(w2_map)
        form = 0
        left = 0

        for r in range(M):
            c = w1[r]
            w1_map[c] += 1

            if c in w2_map and w1_map[c] == w2_map[c]:
                form += 1
            
            while form == requir:
                res += M - r
                left_c = w1[left]
                w1_map[left_c] -= 1

                if left_c in w2_map and w1_map[left_c] < w2_map[left_c]:
                    form -= 1
                left += 1
        
        return res
    

print(Solution().validSubstringCount('bcca', 'abc'))
print(Solution().validSubstringCount("bbbbbbbbbbbbbbb", "bb"))