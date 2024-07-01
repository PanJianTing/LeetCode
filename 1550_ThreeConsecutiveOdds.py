class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:

        count = 0

        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                if count == 2:
                    return True
                count += 1

        return False
    
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        N = len(arr)

        for i in range(N-2):
            if 1 == (arr[i] & 1) == (arr[i+1] & 1) == (arr[i+2] & 1):
                return True
        
        return False

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        N = len(arr)
        cnt = 0

        for i in range(N):
            if arr[i] & 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        
        return False

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        N = len(arr)

        for i in range(N-2):
            if (arr[i] * arr[i+1] * arr[i+2]) & 1:
                return True
        
        return False