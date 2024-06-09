from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        N = len(nums)
        mod_map = defaultdict(list)
        mod_map[0] = [-1]
        prefix_sum = 0
        res = 0
        
        for i in range(N):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            mod_map[mod].append(i)

        for k in mod_map.keys():
            cnt = len(mod_map[k])
            res += (cnt * (cnt - 1)) >> 1

        return res
    
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        N = len(nums)
        mod_map = defaultdict(int)
        mod_map[0] = 1
        prefix_sum = 0
        res = 0

        for i in range(N):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            res += mod_map[mod]
            mod_map[mod] += 1

        return res
    
print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))
print(Solution().subarraysDivByK([5], 9))