import heapq

class Solution:
    def minMeetingRooms(self, A: list[list[int]]) -> int:
        h = []
        sortA = sorted(A)

        for i in sortA:
            if h == [] or h[0] > i[0]:
                heapq.heappush(h, i[1])
            else:
                heapq.heapreplace(h, i[1])
        return len(h)
    
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        hq = []
        intervals.sort()

        for st, end in intervals:
            if hq and hq[0] <= st:
                heapq.heappop(hq)
            heapq.heappush(hq, end)
        return len(hq)
    
    def minMeetingRooms(sefl, intervals: list[list[int]]) -> int:
        N = len(intervals)
        st_times = []
        end_times = []

        for st, end in intervals:
            st_times.append(st)
            end_times.append(end)
        
        st_times.sort()
        end_times.sort()

        st_p = 0
        end_p = 0
        res = 0

        # while st_p < N:
        #     if st_times[st_p] < end_times[end_p]:
        #         res += 1
        #     else:
        #         end_p += 1
        #     st_p += 1

        while st_p < N:
            if st_times[st_p] >= end_times[end_p]:
                res -= 1
                end_p += 1
            res += 1
            st_p += 1
        return res
    
print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))
print(Solution().minMeetingRooms([[2,11],[6,16],[11,16]]))
print(Solution().minMeetingRooms([[2,15],[36,45],[9,29],[16,23],[4,9]]))