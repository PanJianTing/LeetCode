import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], target: int) -> int:
        N = len(times)
        time_hq = []
        full_hq = []
        empty_hq = []
        cur_max_chair = 0
        ans = N

        for i in range(N):
            cur_st, cur_end = times[i]
            heapq.heappush(time_hq, (cur_st, cur_end, i))


        while time_hq:
            cur_st, cur_end, i = heapq.heappop(time_hq)

            while full_hq and full_hq[0][0] <= cur_st:
                _, cur_chair = heapq.heappop(full_hq)
                heapq.heappush(empty_hq, cur_chair)
            
            if empty_hq:
                chair_sit = heapq.heappop(empty_hq)
                if i == target:
                    return chair_sit
                heapq.heappush(full_hq, (cur_end, chair_sit))
            else:
                if i == target:
                    return cur_max_chair
                heapq.heappush(full_hq, (cur_end, cur_max_chair))
                cur_max_chair += 1

        return ans


# print(Solution().smallestChair([[1,4],[2,3],[4,6]], 1))
# print(Solution().smallestChair([[3,10],[1,5],[2,6]], 0))
print(Solution().smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]], 6))

            