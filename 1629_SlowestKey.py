class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        
        slowestK = keysPressed[0]
        slowestTime = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > slowestTime:
                slowestTime = time
                slowestK = key
            elif time == slowestTime:
                if key > slowestK:
                    slowestK = key
        return slowestK
        
    
    def slowestKey_my(self, releaseTimes: list[int], keysPressed: str) -> str:
        
        beforeTime = 0;
        timeDic = {}
        
        for i in range(len(keysPressed)):
            key = keysPressed[i];
            time = releaseTimes[i] - beforeTime
            if time in timeDic:
                timeDic[time].add(key)
            else:
                timeDic[time] = set(key)
            beforeTime = releaseTimes[i]
        
        timeDic = sorted(timeDic.items(), key = lambda x:x[0], reverse=True)
        
        return sorted(next(iter(timeDic))[1])[-1]
            
        

print(Solution.slowestKey(Solution(), [9,29,49,50], "cbcd"))
print("Hello World!")