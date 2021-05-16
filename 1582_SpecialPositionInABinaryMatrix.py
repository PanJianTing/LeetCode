class Solution:
    # 先檢查row有沒有只有1個1，有才要放進去檢查col，沒有就pass
    def numSpecial(self, mat: list[list[int]]) -> int:

        cols = len(mat)
        rows = len(mat[0])

        result = 0

        checkPositions = []

        for i in range(cols):
            row = mat[i]

            if row.count(1) == 1:
                j = row.index(1)
                checkPositions.append([i, j])

        for col, row in checkPositions:
            
            isHaveOtherOne = False

            for c in range(cols):
                if mat[c][row] == 1 and c != col:
                    isHaveOtherOne = True
            
            if isHaveOtherOne == False:
                result += 1

        return result
            


    def numSpecial_my(self, mat: list[list[int]]) -> int:

        cols = len(mat)
        rows = len(mat[0])
        
        checkPositions = []
        result = 0
        for i in range(cols):
            for j in range(rows):
                if mat[i][j] == 1:
                    checkPositions.append([i, j])
        
        for col, row in checkPositions:
            isHaveOtherOne = False

            for r in range(rows):
                if mat[col][r] == 1 and r != row:
                    isHaveOtherOne = True
                    break

            for c in range(cols):
                if mat[c][row] == 1 and c != col:
                    isHaveOtherOne = True
                    break
            
            if isHaveOtherOne == False:
                result += 1

        return result

Solution.numSpecial(Solution(), [[1,0,0],[0,0,1],[1,0,0]])