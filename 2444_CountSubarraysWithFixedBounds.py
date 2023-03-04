class Solution:
    # Time Limit Exceeded
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        res = 0

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                subArray = nums[i:j]
                minS = min(subArray)
                maxS = max(subArray)
                if minS < minK or maxS > maxK:
                    break
                if minS == minK  and maxS == maxK:
                    res += 1

        return res

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        maxPosition = -1
        minPosition = -1
        leftBound = -1
        ans = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                leftBound = i
            if minK == num:
                minPosition = i
            if maxK == num:
                maxPosition = i
            
            ans += max(0, min(maxPosition, minPosition) - leftBound)

        return ans





    
print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5))
print(Solution().countSubarrays([1,1,1,1], 1, 1))