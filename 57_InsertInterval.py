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

# Solution().insert([[1,3],[6,9]], [2,5])
Solution().insert([[1,5]], [2,7])
# Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])