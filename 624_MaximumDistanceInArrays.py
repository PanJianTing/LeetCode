class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        N = len(arrays)

        def checkMin():
            cur_min_idx = 0
            cur_min = float('inf')

            cur_max = float('-inf')

            for i in range(N):
                if arrays[i][0] < cur_min:
                    cur_min = arrays[i][0]
                    cur_min_idx = i

            for i in range(N):
                if arrays[i][-1] > cur_max and cur_min_idx != i:
                    cur_max = arrays[i][-1]
        
            return cur_max - cur_min
        
        def checkMax():
            cur_min = float('inf')

            cur_max_idx = 0
            cur_max = float('-inf')

            for i in range(N):
                if arrays[i][-1] > cur_max:
                    cur_max = arrays[i][-1]
                    cur_max_idx = i

            for i in range(N):
                if arrays[i][0] < cur_min and cur_max_idx != i:
                    cur_min = arrays[i][0]
        
            return cur_max - cur_min
        
        return max(checkMin(), checkMax())
    

    def maxDistance(self, arrays: list[list[int]]) -> int:
        N = len(arrays)
        res = 0

        for i in range(N):
            a1 = arrays[i]
            for j in range(i+1, N):
                a2 = arrays[j]
                for k in a1:
                    for l in a2:
                        res = max(res, abs(k - l))

        return res
    
    def maxDistance(self, arrays: list[list[int]]) -> int:
        N = len(arrays)
        res = 0

        for i in range(N):
            a1 = arrays[i]
            for j in range(i+1, N):
                a2 = arrays[j]
                res = max(res, abs(a1[0] - a2[-1]))
                res = max(res, abs(a1[-1] - a2[0]))

        return res
    
    def maxDistance(self, arrays: list[list[int]]) -> int:
        N = len(arrays)
        max_val = arrays[0][-1]
        min_val = arrays[0][0]
        res = 0
        

        for i in range(1, N):
            res = max(res, arrays[i][-1] - min_val, max_val - arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])

        return res
    
    def maxDistance(self, arrays: list[list[int]]) -> int:
        N = len(arrays)
        pair = set()
        min1, min2, max1, max2 = float('inf'), float('inf'), float('-inf'), float('-inf')

        for cur_list in arrays:
            cur_min, cur_max = cur_list[0], cur_list[-1]

            if min1 > cur_min:
                min2 = min1
                min1 = cur_min
            elif min2 > cur_min:
                min2 = cur_min
            
            if max1 < cur_max:
                max2 = max1
                max1 = cur_max
            elif max2 < cur_max:
                max2 = cur_max
            
            pair.add((cur_min, cur_max))
        
        if (min1, max1) not in pair:
            return max1 - min1
        return max((max1 - min2), (max2 - min1))




    
print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]]))
print(Solution().maxDistance([[1],[1]]))
print(Solution().maxDistance([[1,4],[0,5]]))
print(Solution().maxDistance([[-2],[-3,-2,1]]))