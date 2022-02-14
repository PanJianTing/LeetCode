class Solution:
    def sortColors(self, nums: list):
        
        numsMap = {0:0, 1:0, 2:0}
        
        for color in nums:
            numsMap[color] += 1
            
        ans = [0] * numsMap[0] + [1] * numsMap[1] + [2] * numsMap[2]
        
        for i in range(0, len(nums)):
            nums[i] = ans[i]

class Solution:
    def sortColors(self, nums: list):
        
        curr = 0
        p0 = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            now = nums[curr]
            if now == 2:
                nums[curr] , nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                if now == 0:
                    nums[curr], nums[p0] = nums[p0], nums[curr]
                    p0 += 1
                curr += 1