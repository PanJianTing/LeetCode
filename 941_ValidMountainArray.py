class Solution:

    def validMountainArray(self, arr: list[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        N = len(arr)
        walkStep = 0

        # check UP
        while walkStep + 1 < N and arr[walkStep + 1] > arr[walkStep]:
            walkStep += 1
        
        # 已在山頂或還在山腳
        if walkStep == 0 or walkStep == N - 1:
            return False
        
        # check down
        while walkStep + 1 < N and arr[walkStep + 1] < arr[walkStep]:
            walkStep += 1
            
        # 檢查是否有走完    
        return walkStep == N - 1


    def validMountainArray_for(self, arr: list[int]) -> bool:

        if len(arr) < 3:
            return False

        N = len(arr)
        walkStep = 0

        # check Up
        for i in range(1, N):
            if arr[i-1] < arr[i]:
                walkStep += 1
            else:
                break
        
        if walkStep == 0 or walkStep == N - 1:
            return False
        
        # check Down
        for i in range(1, N):
            if arr[i-1] > arr[i]:
                walkStep += 1
        
        # 檢查是否有走滿
        return walkStep == N-1



    def validMountainArray_my(self, arr: list[int]) -> bool:
        
        if len(arr) < 3:
            return False

        # find max
        maxIndex = 0
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            if arr[i] > arr[maxIndex]:
                maxIndex = i
        
        # maxIndex 不能是最後 or 第一
        if maxIndex + 1 == len(arr) or maxIndex == 0:
            return False

        
        for i in range(1, len(arr)):
            # down
            if i > maxIndex and arr[i-1] < arr[i]:
                return False
            # up
            elif i <= maxIndex and arr[i-1] > arr[i]:
                return False


        return True


Solution.validMountainArray(Solution(), [0, 2, 3, 4, 5, 2, 1, 0])