class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        f = 0
        l = len(mat[0]) - 1
        ans = 0
        for arr in mat:
            ans += arr[f]
            if f != l:
                ans += arr[l]
                
            f += 1
            l -= 1
        return ans
    
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:

        sum = 0

        n = len(mat)

        idx = n-1

        for i in range(0, n):
            sum += mat[i][i]
            sum += mat[i][idx]
            idx -= 1

        if n % 2:
            i = n >> 1
            sum -= mat[i][i]
        return sum
    
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        n = len(mat)
        mid = n >> 1

        for i in range(mid):
            sum += mat[i][i] + mat[i][-1-i] + mat[-1-i][i] + mat[-1-i][-1-i]
        
        if n % 2:
            sum += mat[mid][mid]

        return sum
