class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        total = n * n
        start = 1
        ans = [[0 for _ in range(n)] for _ in range(n)]

        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        visitSet = set()

        cur = 0
        i = 0
        j = 0

        while start <= total:
            while True:
                if (i, j) not in visitSet:
                    # print(i, j)
                    ans[i][j] = start
                    visitSet.add((i,j))
                    start += 1

                next_i = i + direction[cur][0]
                next_j = j + direction[cur][1]

                if (0 <= next_i < n and 0 <= next_j < n) == False:
                    break

                if (next_i, next_j) in visitSet:
                    break

                i = next_i
                j = next_j
            
            cur = (cur+1) % 4

        return ans

print(Solution().generateMatrix(1))    
print(Solution().generateMatrix(3))