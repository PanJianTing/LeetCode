from functools import cache

class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        N = len(nums)
        max_num = 0

        for n in nums:
            max_num |= n

        @cache
        def dp(idx, cur):
            if idx == N:
                if cur == max_num:
                    return 1
                else:
                    return 0
            count_with = dp(idx+1, cur | nums[idx])
            count_no_with = dp(idx+1, cur)
            return count_with + count_no_with
        
        return dp(0, 0)
    
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        N = len(nums)
        max_num = 0

        for n in nums:
            max_num |= n
        
        cache_map = [[-1] * (max_num+1) for _ in range(N)] 

        def dp(idx, cur):
            if idx == N:
                if cur == max_num:
                    return 1
                return 0

            if cache_map[idx][cur] != -1:
                return cache_map[idx][cur]

            ans = 0
            ans += dp(idx+1, cur|nums[idx])
            ans += dp(idx+1, cur)
            cache_map[idx][cur] = ans
            return ans
        return dp(0, 0)


    def countMaxOrSubsets(self, nums: list[int]) -> int:
        N = len(nums)
        max_subset = 1 << N
        max_val = 0
        ans = 0

        for n in nums:
            max_val |= n

        for cur_mask in range(max_subset):

            cur_or = 0

            for i in range(N):
                if (cur_mask >> i) & 1:
                    cur_or |= nums[i]
            
            if cur_or == max_val:
                ans += 1
        
        return ans



print(Solution().countMaxOrSubsets([3,1]))
print(Solution().countMaxOrSubsets([2,2,2]))
print(Solution().countMaxOrSubsets([3,2,1,5]))
        