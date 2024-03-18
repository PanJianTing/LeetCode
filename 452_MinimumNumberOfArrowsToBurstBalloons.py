class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        res = []
        points.sort()

        for cur_st, cur_end in points:
            if res and cur_st <= res[-1][1]:
                st, end = res.pop()
                res.append([max(cur_st, st), min(cur_end, end)])
            else:
                res.append([cur_st, cur_end])
        
        return len(res)
    
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        N = len(points)
        res = 1
        points.sort(key= lambda x : x[1])
    
        cur_end = points[0][1]

        for idx in range(1, N):
            st, end = points[idx]
            
            if cur_end < st:
                res += 1
                cur_end = end
        return res
    

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))