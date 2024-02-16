import heapq

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()
        ans = -1
        sum_perimeter = nums[0] + nums[1]

        for i in range(2, N):
            cur = nums[i]
            if sum_perimeter > cur:
                ans = max(ans, sum_perimeter + cur)
            sum_perimeter += cur

        return ans
    
    def largestPerimeter(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()
        ans = -1
        sum_perimeter = 0

        for cur in nums:
            if sum_perimeter > cur:
                ans = max(ans, sum_perimeter + cur)
            sum_perimeter += cur
        return ans
    
    def largestPerimeter(self, nums: list[int]) -> int:
        all_sum = sum(nums)
        
        while len(nums) > 2:
           cur_max = max(nums)
           cur_edge = all_sum - cur_max
           if cur_edge > cur_max:
               return all_sum
           
           nums.remove(cur_max)
           all_sum -= cur_max
        return -1
    
    def largestPerimeter(self, nums: list[int]) -> int:
        cur_perimeter = sum(nums)
        heapq._heapify_max(nums)
        while nums and cur_perimeter <= (nums[0] << 1):
            cur_perimeter -= heapq._heappop_max(nums)
        return cur_perimeter if len(nums) > 2 else -1
    
print(Solution().largestPerimeter([5,5,5]))
print(Solution().largestPerimeter([1,12,1,2,5,50,3]))
print(Solution().largestPerimeter([5,5,50]))