def diagonalSum(mat: List[List[int]]) -> int:
        f = 0
        l = len(mat[0]) - 1
        ans = 0
        for arr in mat:
            ans += arr[f];
            if f != l:
                ans += arr[l]
                
            f += 1
            l -= 1
        return ans
