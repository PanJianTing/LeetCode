class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])
        ans = [0] * (M * N)
        i = 0
        j = 0
        endI = 0
        endJ = 0
        isAdd = True

        for k in range(len(ans)):
            # print(i , j)
            ans[k] = matrix[i][j]
            if isAdd:
                if j < N-1:
                    j += 1
                elif i < M-1:
                    i += 1
                else:
                    j -= 1
                    isAdd = False
            else:
                if j > endJ:
                    j -= 1
                elif i > endI:
                    i -= 1
                if i == endI and j == endJ:
                    M -= 1
                    N -= 1
                    endI += 1
                    endJ += 1
                    i = endI
                    j = endJ
                    isAdd = True
        return ans
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])
        left = 0
        right = N - 1
        top = 0
        down = M - 1
        ans = []

        while (len(ans) < M * N):
            
            # left to right
            for i in range(left, right+1):
                ans.append(matrix[left][i])
            
            # top to down
            for i in range(top+1, down+1):
                ans.append(matrix[i][right])
            
            # right to left
            if top != down:
                for i in range(right-1, left-1, -1):
                    ans.append(matrix[down][i])

            # down to top
            if left != right:
                for i in range(down-1, top, -1):
                    ans.append(matrix[i][top])

            top += 1
            left += 1
            down -= 1
            right -= 1

        return ans
    

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        visited = 101
        M = len(matrix)
        N = len(matrix[0])
        direction = [[0,1], [1, 0], [0, -1], [-1, 0]]
        currDirection = 0
        changeDirection = 0

        i = 0
        j = 0
        res = [matrix[i][j]]
        matrix[i][j] = visited

        while changeDirection < 2:

            while True:
                next_i = i + direction[currDirection][0]
                next_j = j + direction[currDirection][1]

                if (0 <= next_i < M and 0 <= next_j < N) == False:
                    break

                if matrix[next_i][next_j] == visited:
                    break

                changeDirection = 0
                i = next_i
                j = next_j
                res.append(matrix[i][j])
                matrix[i][j] = visited
            
            currDirection = (currDirection + 1) % 4
            changeDirection += 1

        return res
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(Solution().spiralOrder([[3],[2]]))


# Solution().spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [16,17,18,19,20]])
