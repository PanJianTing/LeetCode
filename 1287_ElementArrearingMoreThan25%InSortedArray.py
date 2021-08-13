class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        overCount = len(arr) // 4

        for i in range(len(arr)):
            if arr[i] == arr[i+overCount]:
                return arr[i]

        return 0


    def findSpecialInteger_my(self, arr: list[int]) -> int:

        countMap = {}

        overCount = len(arr) // 4
        result = 0

        for count in arr:
            if count in countMap:
                countMap[count] += 1
            else:
                countMap[count] = 1
        
        for count in countMap.keys():
            if countMap[count] > overCount and count > result:
                result = count
        return result


Solution.findSpecialInteger(Solution(), [1,2,2,6,6,6,6,7,10])