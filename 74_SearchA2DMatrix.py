class Solution:
    def searchMatrix(self, matrix: list[list[int]], target) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        ml = 0
        mr = m-1

        while ml < mr:
            mm = mr - ((mr - ml) >> 1)
            if matrix[mm][0] <= target:
                ml = mm
            else:
                mr = mm - 1
        
        nl = 0
        nr = n-1

        while nl < nr:
            nm = nr - ((nr - nl) >> 1)
            if matrix[mr][nm] <= target:
                nl = nm
            else:
                nr = nm - 1

        return matrix[ml][nl] == target
    
    def seafrchMatrix(self, matrix: list[list[int]], target) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        ml = 0
        mr = m-1

        while ml <= mr:
            mm = mr - ((mr - ml) >> 1)
            if matrix[mm][0] < target:
                ml = mm + 1
            elif matrix[mm][0] == target:
                return True
            else:
                mr = mm - 1
        
        nl = 0
        nr = n-1

        while nl <= nr:
            nm = nr - ((nr - nl) >> 1)
            if matrix[mr][nm] < target:
                nl = nm + 1
            elif matrix[mr][nm] == target:
                return True
            else:
                nr = nm - 1

        return False
    

    def searcfhMatrix(self, matrix, target) -> int:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = r - ((r - l) >> 1)

            check = matrix[mid // n][mid % n]

            if check < target:
                l = mid + 1
            elif check == target:
                return True
            else:
                r = mid - 1

        return False
    
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution().searchMatrix([[1]], 1))
