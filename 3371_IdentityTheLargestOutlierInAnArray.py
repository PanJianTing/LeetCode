from collections import defaultdict

class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        cnt_map = defaultdict(int)
        all_sum = 0
        ans = float('-inf')

        for n in nums:
            cnt_map[n] += 1
            all_sum += n

        for n in nums:
            cur_sum = all_sum - n
            cnt_map[n] -= 1
            if cnt_map[n] == 0:
                del cnt_map[n]
            if (cur_sum & 1 == 0) and (cur_sum >> 1) in cnt_map:
                ans = max(ans, n)
            cnt_map[n] += 1
        
        return ans
        
        
print(Solution().getLargestOutlier([2,3,5,10]))