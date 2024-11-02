from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        char_pos_map = defaultdict(list)
        res = []

        for i, c in enumerate(s):
            char_pos_map[c].append(i)

        for l, r in queries:
            count = 0

            for pos in char_pos_map.values():

                left_bound = bisect_left(pos, l)
                right_bound = bisect_right(pos, r)
                num_occurrence = right_bound - left_bound

                count += (num_occurrence * (num_occurrence + 1)) >> 1

            res.append(count)

        return res
    

    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        N = len(s)
        char_freq_list = [[0] * N for _ in range(26)]
        res = []

        for i, char in enumerate(s):
            char_freq_list[ord(char) - ord('a')][i] += 1
        
        for char_freq in char_freq_list:
            for i in range(1, N):
                char_freq[i] += char_freq[i-1]
        

        for l, r in queries:

            count = 0

            for char_freq in char_freq_list:
                if l == 0:
                    left_count = 0
                else:
                    left_count = char_freq[l-1]
                freq = char_freq[r] - left_count

                count += (freq * (freq+1)) >> 1
            
            res.append(count)

        return res

    

print(Solution().sameEndSubstringCount("abcaab", [[0,0],[1,4],[2,5],[0,5]]))