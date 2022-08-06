class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        
        rowForZero = set()
        colForZoro = set()

        mIndex = len(matrix)
        nIndex = len(matrix[0])

        for m in range(0, mIndex):
            for n in range(0, nIndex):
                if matrix[m][n] == 0:
                    rowForZero.add(m)
                    colForZoro.add(n)
                # print(m, n, matrix[m][n])
        
        # print(rowForZero)
        # print(colForZoro)

        # for rowIndex in rowForZero:
        #     for n in range(0, nIndex):
        #         matrix[rowIndex][n] = 0
        
        # for colIndex in colForZoro:
        #     for m in range(0, mIndex):
        #         matrix[m][colIndex] = 0
            
        

        for m in range(0, mIndex):
            for n in range(0, nIndex):
                if m in rowForZero or n in colForZoro:
                    matrix[m][n] = 0
                    
        # print(matrix)

        return

# Solution().setZeroes([[1,1,1], [1,0,1], [1,1,1]])
Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])