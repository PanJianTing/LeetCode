from collections import defaultdict

class Solution:
    def findSmallestRegion(self, regions: list[list[str]], region1: str, region2: str) -> str:

        child_parent_map = defaultdict(str)

        for r in regions:
            parent = r[0]
            for idx in range(1, len(r)):
                child = r[idx]
                child_parent_map[child] = parent
        
        def findPath(r):
            cur_r = r
            cur_path = []
            cur_path.append(cur_r)

            while child_parent_map[cur_r]:
                next_r = child_parent_map[cur_r]
                cur_path.append(next_r)
                cur_r = next_r
            
            cur_path.reverse()
            return cur_path

        p1 = findPath(region1)
        p2 = findPath(region2)
        res = ""

        for cur_1, cur_2 in zip(p1, p2):
            if cur_1 == cur_2:
                res = cur_1
            else:
                break
        return res
    

print(Solution().findSmallestRegion([["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]], "Quebec", "New York"))