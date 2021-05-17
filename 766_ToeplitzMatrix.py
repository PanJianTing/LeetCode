class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:

        # for r, row in enumerate(matrix):
        #     for c, val in enumerate(row):
        #         if r != 0 and c != 0:
        #             if matrix[r-1][c-1] != val:
        #                 return False
        # return True


        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val 
                    for r, row in enumerate(matrix)
                    for c, val in enumerate(row))



    def isToeplitzMatrix_my(self, matrix: list[list[int]]) -> bool:

        matrixMap = {}
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                count = matrix[i][j]
                key = j - i
                if key in matrixMap:
                    if matrixMap[key] != count:
                        return False
                else:
                    matrixMap[key] = count
        return True


print(Solution.isToeplitzMatrix(Solution(), [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

print(Solution.isToeplitzMatrix(Solution(), [[1,2],[2,2]])) 