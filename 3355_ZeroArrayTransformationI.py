from collections import defaultdict

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        N = len(nums)
        cnt_map = defaultdict(int)

        for st, end in queries:
            for i in range(st, end+1):
                cnt_map[i] += 1
            
        for i in range(N):
            cur_num = nums[i]
            if cur_num > cnt_map[i]:
                return False
        return True
    
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        N = len(nums)
        freq = defaultdict(int)
        substract_cnt = 0

        for st, end in queries:
            freq[st] += 1
            freq[end+1] -= 1
        
        for i in range(N):
            substract_cnt += freq[i]
            if nums[i] > substract_cnt:
                return False
        return True
        
    

print(Solution().isZeroArray([1,0,1], [[0,2]]))
print(Solution().isZeroArray([4,3,2,1], [[1,3],[0,2]]))