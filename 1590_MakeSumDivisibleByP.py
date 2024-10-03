class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        N = len(nums)
        res = N
        
        total_sum = sum(nums)

        if total_sum % p == 0:
            return 0
        
        for st in range(N):
            sub_sum = 0
            for end in range(st, N):
                sub_sum += nums[end]

                if (total_sum - sub_sum) % p == 0:
                    res = min(res, end-st+1)
        
        return -1 if res == N else res
    

    def minSubarray(self, nums: list[int], p: int) -> int:
        N = len(nums)
        total_sum = sum(nums)
        target = total_sum % p
        mod_map = {}

        if target == 0:
            return 0
        
        mod_map[0] = -1

        cur_sum = 0
        res = N

        for i in range(N):
            cur_sum += nums[i]

            needed = (cur_sum - target + p) % p

            if needed in mod_map:
                res = min(res, i - mod_map[needed])
            
            mod_map[cur_sum % p] = i
        
        return -1 if res == N else res

    

print(Solution().minSubarray([3,1,4,2], 6))
print(Solution().minSubarray([6,3,5,2], 9))
