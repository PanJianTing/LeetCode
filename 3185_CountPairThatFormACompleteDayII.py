from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        cnt_list = [0] * 24
        res = 0

        for h in hours:
            need = (24 - (h % 24)) % 24
            res += cnt_list[need]
            cnt_list[h % 24] += 1

        return res
    
print(Solution().countCompleteDayPairs([12,12,30,24,24]))
print(Solution().countCompleteDayPairs([72,48,24,3]))
print(Solution().countCompleteDayPairs([13, 11]))
