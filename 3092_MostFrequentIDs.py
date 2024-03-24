from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        cnt_map = defaultdict(int)
        h = []
        ans = []

        for cur_id, cur_freq in zip(nums, freq):
            cnt_map[cur_id] += cur_freq
            heapq.heappush(h, (-cnt_map[cur_id], cur_id))
            while h and -cnt_map[h[0][1]] != h[0][0]:
                heapq.heappop(h)

            ans.append(-h[0][0])

        return ans

print(Solution().mostFrequentIDs([2,3,2,1], [3,2,-3,1]))
print(Solution().mostFrequentIDs([5,5,3], [2,-2,1]))
        
    