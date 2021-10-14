class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:

        arr = sorted(arr)

        minimum = float('inf')
        res = []

        for i in range(0, len(arr) - 1):
            a = arr[i]
            b = arr[i+1]
            diff = b-a
            if diff < minimum:
                res = []
                res.append([a, b])
                minimum = diff
            elif diff == minimum:
                res.append([a,b])
            
        return res