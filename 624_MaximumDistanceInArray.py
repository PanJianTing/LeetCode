import heapq

class Solution:
    def maxDistance(self, arrays) -> int:
        M = len(arrays)
        min_array = []
        max_array = []

        for i in range(M):
            min_array.append(arrays[i][0])
            max_array.append(arrays[i][-1])
        
        max_num = 0
        for i in range(M):
            for j in range(M):
               if i != j:
                   max_num = max(max_num, max_array[i] - min_array[j])
        
        return max_num
    
    def maxDistance(self, arrays) -> int:
        M = len(arrays)
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = 0

        for i in range(1, M):
            cur_array = arrays[i]
            res = max(res, abs(cur_array[-1] - min_val), abs(max_val - cur_array[0]))
            max_val = max(max_val, cur_array[-1])
            min_val = min(min_val, cur_array[0])

        return res
        

print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]]))
print(Solution().maxDistance([[1],[1]]))
print(Solution().maxDistance([[-2],[-3,-2,1]]))