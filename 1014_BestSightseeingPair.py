class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        cur = 0
        ans = 0

        for v in values:
            ans = max(ans, cur + v)
            cur = max(cur, v) - 1
        
        return ans
    
print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))