class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:

        totalLength = len(arr)

        resList = []

        for num in arr:
            resList.append(num)
            if num == 0:
                resList.append(num)

        for i in range(0, totalLength):
            arr[i] = resList[i]

        return

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:

        totalLength = len(arr)
        zeros = arr.count(0)

        for i in range(totalLength-1, -1 ,-1):
            if i+zeros < totalLength:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < totalLength:
                    arr[i+zeros] = 0
        




Solution().duplicateZeros([1,0,2,3,0,4,5,0])