import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        use_meeting_rooms = [0] * n
        end_meeting_rooms = [0] * n

        for st, end in meetings:
            select_idx = n
            cur_fast_idx = 0
            for i in range(n):
                if st >= end_meeting_rooms[i]:
                    select_idx = min(select_idx, i)
                else:
                    fast_idx = cur_fast_idx
                    if end_meeting_rooms[fast_idx] > end_meeting_rooms[i]:
                        cur_fast_idx = i
            if select_idx != n:
                end_meeting_rooms[select_idx] = end
                use_meeting_rooms[select_idx] += 1
            else:
                end_meeting_rooms[cur_fast_idx] = end_meeting_rooms[cur_fast_idx] + (end-st)
                use_meeting_rooms[cur_fast_idx] += 1
        
        ans_idx = 0
        max_count = use_meeting_rooms[0]

        for i in range(1, n):
            if max_count < use_meeting_rooms[i]:
                ans_idx = i
                max_count = use_meeting_rooms[i]
        
        return ans_idx
    

    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        meeting_rooms_use = [0] * n
        empty_room = [i for i in range(n)]
        using_room = [] #(end_time, idx)

        for st, end in meetings:
            while using_room and st >= using_room[0][0]:
                _, cur_idx = heapq.heappop(using_room)
                heapq.heappush(empty_room, cur_idx)
                
            if len(empty_room) > 0:
                select_room = heapq.heappop(empty_room)
                heapq.heappush(using_room, (end, select_room))
            else:
                select_end_time, select_room = heapq.heappop(using_room)
                heapq.heappush(using_room, (select_end_time + (end-st), select_room))
                
            meeting_rooms_use[select_room] += 1

        max_idx = 0
        max_cnt = meeting_rooms_use[max_idx]
        for i in range(1, n):
            if meeting_rooms_use[i] > max_cnt:
                max_cnt = meeting_rooms_use[i]
                max_idx = i

        return max_idx
    
print(Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
print(Solution().mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))
print(Solution().mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]]))

