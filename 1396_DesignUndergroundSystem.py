from collections import defaultdict

class UndergroundSystem:
    stationTime = {}
    allTime = {}

    def __init__(self):
        self.stationTime = {}
        self.allTime = {}
        

    def checkIn(self, id: int, stationName: str, t: int):
        if id in self.stationTime:
            self.stationTime[id][stationName] = t
        else:
            temp = {}
            temp[stationName] = t
            self.stationTime[id] = temp


    def checkOut(self, id: int, stationName: str, t: int):
        if id in self.stationTime:
            for key in self.stationTime[id].keys():
                timeKey = stationName + "/" + key
                if timeKey in self.allTime:
                    (allTime, cnt) = self.allTime[timeKey]
                    allTime += (t - self.stationTime[id][key])
                    cnt += 1
                    self.allTime[timeKey] = (allTime, cnt)
                else:
                    self.allTime[timeKey] = (t - self.stationTime[id][key], 1)

            del self.stationTime[id]


    def getAverageTime(self, start: str, end: str) -> float:
        timeKey = end + "/" + start
        (s,c) = self.allTime[timeKey]
        return s / c
    

class UndergroundSystem:
    stationTime = {}
    allTime = {}

    def __init__(self):
        self.stationTime = {}
        self.allTime = {}
        

    def checkIn(self, id: int, stationName: str, t: int):
        self.stationTime[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int):

        (start, startT) = self.stationTime.pop(id)
        key = stationName + '/' + start
        if key in self.allTime:
            totalT, cnt = self.allTime[key]
            self.allTime[key] = (totalT + (t-startT), cnt+1)
        else:
            self.allTime[key] = (t-startT, 1)


    def getAverageTime(self, start: str, end: str) -> float:
        timeKey = end + "/" + start
        (s,c) = self.allTime[timeKey]
        return s / c
    

class UndergroundSystem:
    stationTime = {}
    allTime = defaultdict(lambda : [0,0])

    def __init__(self):
        self.stationTime = {}
        self.allTime = defaultdict(lambda : [0,0])
        

    def checkIn(self, id: int, stationName: str, t: int):
        self.stationTime[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int):

        (start, startT) = self.stationTime.pop(id)
        key = stationName + '/' + start
        self.allTime[key][0] += (t-startT)
        self.allTime[key][1] += 1


    def getAverageTime(self, start: str, end: str) -> float:
        timeKey = end + "/" + start
        [s,c] = self.allTime[timeKey]
        return s / c