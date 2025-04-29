class Solution:
    def countSubarray(self, nums: list[int], k: int) -> int:
        N = len(nums)
        max_num = max(nums)
        cur_cnt = 0
        res = 0
        st = 0

        for end in range(N):
            if nums[end] == max_num:
                cur_cnt += 1
            while  cur_cnt == k:
                if nums[st] == max_num:
                    cur_cnt -= 1
                st += 1
            res += st
        
        return res
    
print(Solution().countSubarray([1,3,2,3,3], 2))

print(Solution().countSubarray([4,3,7,10,2,10,1,6,10,7,10,10,9,8,3], 3))

        