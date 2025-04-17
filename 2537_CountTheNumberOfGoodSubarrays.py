from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cur_same = 0
        right = -1
        cnt_map = defaultdict(int)
        ans = 0

        for l in range(N):
            while cur_same < k and right + 1 < N:
                right += 1
                cur_same += cnt_map[nums[right]]
                cnt_map[nums[right]] += 1

            if cur_same >= k:
                ans += N - right
            cnt_map[nums[l]] -= 1
            cur_same -= cnt_map[nums[l]]
        
        return ans
    
print(Solution().countGood([1,1,1,1,1], 10))
print(Solution().countGood([3,1,4,3,2,2,4], 2))