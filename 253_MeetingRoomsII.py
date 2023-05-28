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