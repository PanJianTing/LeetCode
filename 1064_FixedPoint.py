class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        for i in range(len(arr)):
            if arr[i] == i:
                return arr[i]
        return -1