import bisect
class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        N = len(nums)
        cnt = 0
        for n in nums:
            if n == target:
                cnt += 1

        return cnt > (N//2)
    
    def isMajorityElement(self, nums, T) -> bool:
        N = len(nums)
        lIdx = bisect.bisect_left(nums, T)
        rIdx = bisect.bisect_right(nums, T)

        
        print(lIdx)
        print(rIdx)
        print(rIdx - lIdx)

        return (rIdx - lIdx) > (N//2)
    

print(Solution().isMajorityElement([2,4,5,5,5,5,5,6,6], 5))

