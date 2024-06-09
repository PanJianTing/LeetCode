from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        N = len(nums)
        prefix_list = [0] * N
        prefix_list[0] = nums[0]
        mod_map = defaultdict(list)
        mod_map[0] = [-1]

        for i in range(1, N):
            prefix_list[i] = nums[i] + prefix_list[i-1]

        for i in range(N):
            mod_map[(prefix_list[i] % k)].append(i)
        
        for k in mod_map.keys():
            if len(mod_map[k]) > 2:
                return True
            if len(mod_map[k]) == 2 and (mod_map[k][1] - mod_map[k][0]) > 1:
                return True
        
        return False
    

print(Solution().checkSubarraySum([23,2,4,6,7], 6))
print(Solution().checkSubarraySum([23,2,4,6,6], 7))