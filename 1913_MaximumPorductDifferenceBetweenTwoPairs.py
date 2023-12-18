class Solution:
    def maxProductDifference(self, nums) -> int:
        max1 = 0
        max2 = 0
        min1 = float('inf')
        min2 = float('inf')

        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
            
            if min1 > n:
                min2 = min1
                min1 = n
            elif min2 > n:
                min2 = n

        return max2 * max1 - (min1 * min2)
    
print(Solution().maxProductDifference([5,6,2,7,4]))
print(Solution().maxProductDifference([4,2,5,9,7,4,8]))
