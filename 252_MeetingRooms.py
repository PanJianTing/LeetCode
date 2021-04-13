
class Solution:
	# 先照開始時間排序，如果這個meeting的結束時間 > 下個meeting的開始時間，則就趕不上meeting
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        
        sortInterval = sorted(intervals, key=lambda x:x[0])
        for i in range(0, len(sortInterval) - 1):
            if sortInterval[i][1] > sortInterval[i+1][0]:
                return False
        return True
    
    def canAttendMeetings_my(self, intervals: list[list[int]]) -> bool:
        
        scheduleMap = set()
        
        for meeting in intervals:
            for time in range(meeting[0], meeting[1]):
                if time in scheduleMap:
                    return False
                else:
                    scheduleMap.add(time)
        
        return True
        
print(Solution.canAttendMeetings(Solution(), [[0,30],[5,10],[15,20]]))
print(Solution.canAttendMeetings(Solution(), [[7,10],[2,4]]))
print("Hello World!")