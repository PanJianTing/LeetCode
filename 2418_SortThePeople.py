from collections import defaultdict, OrderedDict

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        pair_list = []
        res = []

        for h, n in zip(heights, names):
            pair_list.append((h, n))
        
        pair_list.sort()

        for h, n in pair_list:
            res.append(n)
        
        return res[::-1]
    
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_map = defaultdict(str)
        res = []

        for h, n in zip(heights, names):
            height_map[h] = n
        
        heights.sort()

        for h in heights:
            res.append(height_map[h])
        return res[::-1]
    
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        height_map = OrderedDict()

        for h, n in zip(heights, names):
            height_map[h] = n

        height_map = OrderedDict(sorted(height_map.items(), reverse=True))

        res = list(height_map.values())

        return res
    
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        N = len(names)
        res = []
        sorted_idx = [i for i in range(N)]

        sorted_idx = sorted(sorted_idx,  key= lambda i: heights[i], reverse=True)

        for i in sorted_idx:
            res.append(names[i])
        
        return res

print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))
print(Solution().sortPeople(["Alice","Bob","Bob"], [155,185,150]))
