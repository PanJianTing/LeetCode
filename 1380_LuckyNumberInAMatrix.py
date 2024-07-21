class Soltion:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])
        lucky_cols = [0] * M
        res = []

        for i in range(M):
            temp = float('inf')
            for j in range(N):
                if matrix[i][j] < temp:
                    temp = matrix[i][j]
                    lucky_cols[i] = j

        for row, col in enumerate(lucky_cols):
            temp_idx = 0
            for i in range(M):
                if matrix[i][col] > matrix[temp_idx][col]:
                    temp_idx = i
            if temp_idx == row:
                res.append(matrix[temp_idx][col])
        return res
    

    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])
        row_min = [float('inf')] * M
        col_max = [0] * N
        res = []

        for i in range(M):
            for j in range(N):
                row_min[i] = min(row_min[i], matrix[i][j])

        for j in range(N):
            for i in range(M):
                col_max[j] = max(col_max[j], matrix[i][j])

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == row_min[i] == col_max[j]:
                    res.append(matrix[i][j])

        return res
    
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])
        r_max = 0
        c_min = float('inf')

        for i in range(M):
            temp_min = float('inf')
            for j in range(N):
                temp_min = min(temp_min, matrix[i][j])
            r_max = max(r_max, temp_min)
        
        for j in range(N):
            temp_max = 0
            for i in range(M):
                temp_max = max(temp_max, matrix[i][j])
            c_min = min(c_min, temp_max)
        
        if r_max == c_min:
            return [r_max]

        return []


print(Soltion().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])) #[15]
print(Soltion().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])) #[12]
print(Soltion().luckyNumbers([[7,8],[1,2]])) #[7]
print(Soltion().luckyNumbers([[3,6],[7,1],[5,2],[4,8]])) #[]