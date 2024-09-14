class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = 0
        cur_longest = 0
        ans = 0

        for n in nums:
            if max_val < n:
                max_val = n
                cur_longest = 0
                ans = 0
                
            if max_val == n:
                cur_longest += 1
            else:
                cur_longest = 0
            
            ans = max(ans, cur_longest)

        return ans
    
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = 0
        cur_longest = 0
        ans = 0

        for n in nums:
            if max_val < n:
                max_val = n
                cur_longest = 1
                ans = 1
            elif max_val == n:
                cur_longest += 1
            else:
                cur_longest = 0
            ans = max(ans, cur_longest)
        return ans
    

    
print(Solution().longestSubarray([1,2,3,3,2,2]))
print(Solution().longestSubarray([1,2,3,4]))
print(Solution().longestSubarray([96317,96317,96317,96317,96317,96317,96317,96317,96317,279979]))