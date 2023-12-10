from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        i = 0
        j = 0
        ans = 0
        cnt_map = defaultdict(int)
        N = len(nums)

        while j < N:
            cur = nums[j]
            if cnt_map[cur] + 1 <= k:
                cnt_map[cur] += 1
                j += 1
            else:
                while i < j:
                    cur_delete = nums[i]
                    cnt_map[cur_delete] -= 1
                    i += 1
                    if cur_delete == cur:
                        break
            ans = max(ans, j-i)

        return ans
    

    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        i = 0
        j = 0
        ans = 0
        cnt_map = defaultdict(int)
        N = len(nums)

        while j < N:
            cur = nums[j]
            if cnt_map[cur] + 1 <= k:
                cnt_map[cur] += 1
                j += 1
            else:
                while cnt_map[cur] >= k:
                    cnt_map[nums[i]] -= 1
                    i += 1
            ans = max(ans, j-i)

        return ans
    
    def maxSubarrayLength(self, A, k):
        i = 0
        ans = 0
        N = len(A)
        cnt_map = defaultdict(int)

        for j in range(N):
            cnt_map[A[j]] += 1
            while cnt_map[A[j]] > k:
                cnt_map[A[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
    
print(Solution().maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
print(Solution().maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
print(Solution().maxSubarrayLength([5,5,5,5,5,5,5], 4))
print(Solution().maxSubarrayLength([1,1,1,3], 2))