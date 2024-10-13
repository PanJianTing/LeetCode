from collections import defaultdict
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        N = len(nums)
        indices = [0] * N
        ans = [0, float('inf')]

        while True:
            cur_min, cur_max = float('inf'), float('-inf')
            min_idx = 0

            for i in range(N):
                cur_num = nums[i][indices[i]]

                if cur_num < cur_min:
                    cur_min = cur_num
                    min_idx = i
                
                if cur_num > cur_max:
                    cur_max = cur_num
            
            if cur_max - cur_min < ans[1] - ans[0]:
                ans[1] = cur_max
                ans[0] = cur_min
            
            indices[min_idx] += 1
            if indices[min_idx] == len(nums[min_idx]):
                break
        return ans
    
    def smallestRange(self, nums: list[list[int]]) -> list[int]:

        N = len(nums)
        hq = []
        max_val = float('-inf')
        ans_st = 0
        ans_end = float('inf')

        for i in range(N):
            heapq.heappush(hq, [nums[i][0], i, 0])
            max_val = max(max_val, nums[i][0])

        while len(hq) == N:
            min_val, list_idx, num_idx = heapq.heappop(hq)

            if max_val - min_val < ans_end - ans_st:
                ans_st = min_val
                ans_end = max_val
            
            if num_idx + 1 < len(nums[list_idx]):
                heapq.heappush(hq, [nums[list_idx][num_idx+1], list_idx, num_idx + 1])
                max_val = max(max_val, nums[list_idx][num_idx+1])
        
        return [ans_st, ans_end]
    

    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        N = len(nums)
        merged = []
        ans_st, ans_end = 0, float('inf')

        for i in range(N):
            for n in nums[i]:
                merged.append((n, i))

        merged.sort()
        freq = defaultdict(int)
        l = 0
        count = 0


        for r in range(len(merged)):
            freq[merged[r][1]] += 1
            if freq[merged[r][1]] == 1:
                count += 1

            while count == N:
                cur_range = merged[r][0] - merged[l][0]

                if cur_range < ans_end - ans_st:
                    ans_st = merged[l][0]
                    ans_end = merged[r][0]

                freq[merged[l][1]] -= 1
                if freq[merged[l][1]] == 0:
                    count -= 1
                l += 1
        return [ans_st, ans_end]


    
print(Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(Solution().smallestRange([[1,2,3],[1,2,3],[1,2,3]]))