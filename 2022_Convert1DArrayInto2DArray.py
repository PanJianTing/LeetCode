class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        N = len(original)
        if m * n != N:
            return []

        res = []
        temp = []

        for num in original:
            temp.append(num)
            if len(temp) == n:
                res.append(temp)
                temp = []
        return res
    

    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        N = len(original)
        if m * n != N:
            return []

        res = [[0] * n for _ in range(m)]

        for i, num in enumerate(original):
            res[i // n][i % n] = num
        return res
    
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        N = len(original)
        if m * n != N:
            return []
        
        res = [[0] * n for _ in range(m)]
        idx = 0

        for i in range(m):
            for j in range(n):
                res[i][j] = original[idx]
                idx += 1
        return res
    
print(Solution().construct2DArray([1,2,3,4], 2, 2))
print(Solution().construct2DArray([1,2,3], 1, 2))