
from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr, diff) -> int:
        ans = 0
        N = len(arr)

        for i in range(N):
            temp = 1
            find = arr[i] + diff
            for j in range(i+1, N):
                if arr[j] == find:
                    find += diff
                    temp += 1
            ans = max(ans, temp)

        return ans
    
    def longestSubsequence(self, arr, diff) -> int:
        
        dp = defaultdict(int)
        ans = 1
        N = len(arr)

        for i in range(N):
            dp[arr[i]] = dp[arr[i] - diff] + 1
            ans = max(ans, dp[arr[i]])
        
        return ans

    

print(Solution().longestSubsequence([1,2,3,4], 1))
# print(Solution().longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], 0))