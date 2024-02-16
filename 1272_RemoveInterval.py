class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemove: list[int]) -> list[list[int]]:
        ans = []
        N = len(intervals)
        remove_st = toBeRemove[0]
        remove_end = toBeRemove[1]

        for i in range(N):
            st, end = intervals[i]

            if st < remove_st and remove_st <= end < remove_end:
                ans.append([st, remove_st])
            elif remove_st <= st < remove_end and end > remove_end:
                ans.append([remove_end, end])
            elif st <= remove_st < remove_end < end:
                ans.append([st, remove_st])
                ans.append([remove_end, end])
            elif end < remove_st or st > remove_end:
                ans.append([st, end])
        return ans
    

    def removeInterval(self, intervals: list[list[int]], toBeRemove: list[int]) -> list[list[int]]:
        ans = []
        remove_st = toBeRemove[0]
        remove_end = toBeRemove[1]

        for cur in intervals:
            st, end = cur
            
            if end < remove_st or st > remove_end:
                ans.append(cur)
            else:
                if st < remove_st:
                    ans.append([st, remove_st])
                if end > remove_end:
                    ans.append([remove_end, end])
        return ans
     

print(Solution().removeInterval([[0,2],[3,4],[5,7]], [1,6]))
print(Solution().removeInterval([[0,5]], [2,3]))
print(Solution().removeInterval([[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], [-1,4]))
print(Solution().removeInterval([[0,100]], [50,100]))


        