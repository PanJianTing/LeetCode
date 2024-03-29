class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        max_num = max(nums)
        max_cnt = 0
        st = 0
        res = 0

        for end in range(N):
            if nums[end] == max_num:
                max_cnt += 1
            
            while max_cnt == k:
                if nums[st] == max_num:
                    max_cnt -= 1
                st += 1
            res += st
        return res
    
    def countSubarrays(self, nums: list[int], k: int) -> int:
        idx_list = []
        max_num = max(nums)
        res = 0
        
        for i, n in enumerate(nums):
            if n == max_num:
                idx_list.append(i)

            cur_cnt = len(idx_list)

            if cur_cnt >= k:
                res += idx_list[cur_cnt-k] + 1
        
        return res

        

            
print(Solution().countSubarrays([1,3,2,3,3], 2))
print(Solution().countSubarrays([2,1,3,2,3,2,3], 2))