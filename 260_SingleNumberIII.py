from collections import defaultdict

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        N = len(nums)
        cnt_map = defaultdict(int)
        res = []

        for i in range(N):
            cnt_map[nums[i]] += 1

        for k in cnt_map.keys():
            if cnt_map[k] == 1:
                res.append(k)

        return res
    
    def singleNumber(self, nums: list[int]) -> list[int]:

        bit_mask = 0

        for n in nums:
            bit_mask ^= n
        
        diff = bit_mask & (-bit_mask)

        x = 0
        
        for n in nums:
            if n & diff:
                x ^= n
        
        return [x, bit_mask^x]


print(Solution().singleNumber([1,2,1,3,2,5]))
print(Solution().singleNumber([-1, 0]))
print(Solution().singleNumber([0, 1]))