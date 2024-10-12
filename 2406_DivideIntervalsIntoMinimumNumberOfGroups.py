from collections import defaultdict
import heapq

class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        group_st = []
        intervals.sort()

        for st, end in intervals:
            
            if group_st and group_st[0] < st:
                heapq.heappop(group_st)
            heapq.heappush(group_st, end)
        
        return len(group_st)
    

    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        cur = 0
        ans = 0

        for st, end in intervals:
            events.append((st, 1))
            events.append((end+1, -1))
        
        events.sort()

        for st, plus in events:
            cur += plus
            ans = max(ans, cur)

        return ans
    
    def minGroups(self, intervals: list[list[int]]) -> int:
        count_map = defaultdict(int)
        cur = 0
        ans = 0

        for st, end in intervals:
            count_map[st] += 1
            count_map[end+1] -= 1
        
        for key in sorted(count_map.keys()):
            cur += count_map[key]
            ans = max(ans, cur)

        return ans
    
    def minGroups(self, intervals: list[list[int]]) -> int:
        min_st = float('inf')
        max_end = float('-inf')

        for st, end in intervals:
            min_st = min(min_st, st)
            max_end = max(max_end, end+1)
        
        ranges = [0] * (max_end + 1)
        cur = 0
        ans = 0

        for st, end in intervals:
            ranges[st] += 1
            ranges[end+1] -= 1
        
        for i in range(min_st, max_end+1):
            cur += ranges[i]
            ans = max(ans, cur)
        
        return ans

        
    
print(Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
print(Solution().minGroups([[1,3],[5,6],[8,10],[11,13]]))