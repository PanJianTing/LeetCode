class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        
        rowSmallIndex = set()

        for m in range(0, len(matrix)):
            row = matrix[m]
            nowSmall = 999999
            smallIndex = (-1,-1)
            for n in range(0, len(row)):
                num = row[n]
                if num < nowSmall:
                    nowSmall = num
                    smallIndex = (m,n)

            rowSmallIndex.add(smallIndex)

        res = []

        for index in rowSmallIndex:
            m,n = index
            maxNum = matrix[m][n]
            for row in matrix:
                if row[n] > maxNum:
                    maxNum = -1
                    break
            if maxNum == -1:
                continue
            res.append(maxNum)
        
        return res


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        
        l = list(zip(*matrix))
        res = []
        
        for row in matrix:
            num = min(row)
            j = row.index(num)
            if max(l[j]) == num:
                res.append(num)
        
        return res



Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
Solution().luckyNumbers([[7,8],[1,2]])
        