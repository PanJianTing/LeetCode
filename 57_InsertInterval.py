class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if intervals == []:
            return [newInterval]

        insertResult = []

        for interval in intervals:
            if newInterval != None and interval[0] > newInterval[0]:
                insertResult.append(newInterval)
                newInterval = None
            
            insertResult.append(interval)

        if newInterval != None:
            insertResult.append(newInterval)

        res = []
        res.append(insertResult[0])

        for interval in insertResult:
            lastInterval = res.pop()
            if lastInterval[1] >= interval[0]:
                inter = [min(lastInterval[0], interval[0]), max(lastInterval[1], interval[1])]
                res.append(inter)
            else:
                res.append(lastInterval)
                res.append(interval)

        return res
    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        N = len(intervals)
        res = []
        cur_idx = 0

        # case1: Before interval
        while cur_idx < N and intervals[cur_idx][1] < newInterval[0]:
            res.append(intervals[cur_idx])
            cur_idx += 1

        # case2: in interval
        while cur_idx < N and (False == (newInterval[1] < intervals[cur_idx][0])):
            newInterval[0] = min(newInterval[0], intervals[cur_idx][0])
            newInterval[1] = max(newInterval[1], intervals[cur_idx][1])
            cur_idx += 1
        res.append(newInterval)

        # case3: after interval
        while cur_idx < N:
            res.append(intervals[cur_idx])
            cur_idx += 1
        return res
    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        N = len(intervals)

        l = 0
        r = N-1
        while l <= r:
            m = l + ((r-l) >> 1)

            if intervals[m][0] < newInterval[0]:
                l = m+1
            else:
                r = m-1

        interval_list = []
        for i in range(l):
            interval_list.append(intervals[i])
        interval_list.append(newInterval)

        for i in range(l, N):
            interval_list.append(intervals[i])
        
        res = []
        for i in range(N+1):
            if len(res) == 0 or res[-1][1] < interval_list[i][0]:
                res.append(interval_list[i])
            else:
                res[-1][0] = min(res[-1][0], interval_list[i][0])
                res[-1][1] = max(res[-1][1], interval_list[i][1])

        return res



print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,5]], [2,7]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))