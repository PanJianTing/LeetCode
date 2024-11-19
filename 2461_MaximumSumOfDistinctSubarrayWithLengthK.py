from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cur_sum = 0
        ans = 0
        cnt_map = defaultdict(int)

        for i in range(N):
            if i >= k:
                remove_num = nums[i-k]
                cnt_map[remove_num] -= 1
                if cnt_map[remove_num] == 0:
                    del cnt_map[remove_num]
                cur_sum -= remove_num
            cur_sum += nums[i]
            cnt_map[nums[i]] += 1
            if len(cnt_map) == k:
                ans = max(ans, cur_sum)
        
        return ans
    
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        N = len(nums)
        st = 0
        idx_map = {}
        cur_sum = 0
        ans = 0

        for end in range(N):
            cur_num = nums[end]
            last_idx = idx_map.get(cur_num, -1)

            while st <= last_idx or end - st + 1 > k:
                cur_sum -= nums[st]
                st += 1

            idx_map[cur_num] = end
            cur_sum += cur_num
            
            if end - st + 1 == k:
                ans = max(cur_sum, ans)
        return ans
    
# print(Solution().maximumSubarraySum([1,5,4,2,9,9,9], 3))
print(Solution().maximumSubarraySum([1,2,2], 2))