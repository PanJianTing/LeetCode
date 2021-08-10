class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        temp = [0] * len(arr)
        while temp != arr:
            temp = arr[:]
            for i in range(1, len(temp) - 1):
                arr[i] += (temp[i-1] > temp[i] < temp[i+1]) - (temp[i-1] < temp[i] > temp[i+1])
        return arr

    def transformArray_my(self, arr: list[int]) -> list[int]:
        while True:
            hasChange = False
            temp = list(arr)
            for i in range(1, len(arr) - 1):
                if arr[i-1] > arr[i] < arr[i+1]:
                    temp[i] += 1
                    hasChange = True
                elif arr[i-1] < arr[i] > arr[i+1]:
                    temp[i] -= 1
                    hasChange = True
            arr = temp

            if hasChange == False:
                return arr
        
            
Solution.transformArray(Solution(),[1,6,3,4,3,5])