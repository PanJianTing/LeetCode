class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes, key= lambda x:x[1], reverse = True)
        maxCapacity = 0
        
        for box in boxTypes:
            unit = box[1]
            count = box[0]
            if truckSize > count:
                maxCapacity += count * unit
                truckSize -= count
            else:
                maxCapacity += truckSize * unit
                break
                
        return maxCapacity
    
    def maximumUnits_my(self, boxTypes: list[list[int]], truckSize: int) -> int:
        
        boxCount = {}
        
        for box in boxTypes:
            if box[1] in boxCount:
                boxCount[box[1]] += box[0]
            else:
                boxCount[box[1]] = box[0]
        
        sortBox = sorted(boxCount.keys(), reverse = True)
        maxCapacity = 0
        
        print(boxCount, sortBox)
        
        for box in sortBox:
            # print(box, boxCount[box], truckSize)
            if truckSize >= boxCount[box]:
                maxCapacity += boxCount[box] * box
                truckSize -= boxCount[box]
            else:
                maxCapacity += truckSize * box
                truckSize = 0
            if truckSize == 0:
                break
            
        return maxCapacity
print(Solution.maximumUnits(Solution(), [[5,10],[2,5],[4,7],[3,9]], 10))
print(Solution.maximumUnits(Solution(), [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]], 13))

print("Hello World!")