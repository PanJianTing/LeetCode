class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()
        ans = 0

        def low_bound(l, r, target):

            while l <= r:
                m = l + ((r-l) >> 1)
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            
            return l
        
        for i in range(N):
            cur = nums[i]

            low = low_bound(i+1, N-1, lower - cur)
            hight = low_bound(i+1, N-1, upper - cur + 1)

            ans += (hight - low)
    
        return ans
    
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()

        def lower_bound(val):
            l = 0
            r = N-1
            res = 0

            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum < val:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            return res
        return lower_bound(upper + 1) - lower_bound(lower)

                

print(Solution().countFairPairs([0,1,7,4,4,5], 3, 6))