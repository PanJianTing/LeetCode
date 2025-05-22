import heapq

class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        N = len(nums)
        q = sorted(queries)
        hq = []
        diff = [0] * (N+1)
        cur_diff = 0
        j = 0

        for i in range(N):
            cur_num = nums[i]
            cur_diff += diff[i]

            while j < len(q) and q[j][0] == i:
                heapq.heappush(hq, -1 * q[j][1])
                j += 1
            
            while cur_diff < cur_num and hq and (hq[0] * -1) >= i:
                cur_diff += 1
                diff[(heapq.heappop(hq) * -1) + 1] -= 1
            if cur_diff < cur_num:
                return -1
        return len(hq)

    


print(Solution().maxRemoval([1,2], [[1,1],[0,0],[1,1],[1,1],[0,1],[0,0]]))
# print(Solution().maxRemoval([0,3], [[0,1],[0,0],[0,1],[0,1],[0,0]]))
# print(Solution().maxRemoval([2,0,2], [[0,2],[0,2],[1,1]]))



