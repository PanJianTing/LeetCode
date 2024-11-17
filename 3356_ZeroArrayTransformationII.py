from collections import defaultdict

class Solution:

    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        N = len(nums)
        l = 0
        r = len(queries)
        
        def isZeroArray(k) -> bool:
            
            freq = defaultdict(int)
            substract_cnt = 0

            for i in range(k):
                (st, end, val) = queries[i]
                freq[st] += val
                freq[end+1] -= val
            
            for i in range(N):
                substract_cnt += freq[i]
                if nums[i] > substract_cnt:
                    return False
            return True
        
        while l <= r:
            m = l + ((r-l) >> 1)

            if isZeroArray(m):
                r = m - 1
            else:
                l = m + 1

        return  l if l <= len(queries) else -1


        
    

print(Solution().minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))
print(Solution().minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))