from collections import defaultdict

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        cnt_map = defaultdict(int)

        for n in nums:
            cnt_map[n] += 1
        
        idx = 0

        for n in range(3):
            while cnt_map[n] > 0:
                cnt_map[n] -= 1
                nums[idx] = n
                idx += 1


    def sortColors(self, nums: list[int]) -> None:
        N = len(nums)
        l = 0
        r = N-1
        idx = 0

        while idx <= r:
            if nums[idx] == 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                l += 1

            if nums[idx] == 2:
                nums[idx], nums[r] = nums[r], nums[idx]
                r -= 1
                continue
            idx += 1
        print(nums)
        

print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([2,0,1]))
print(Solution().sortColors([1,2,0]))
