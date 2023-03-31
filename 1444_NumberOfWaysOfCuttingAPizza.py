class Solution:
    def cuts(self, x: int, y: int, rows: int, cols: int, k: int, memo: dict, apples: list[list[int]]) -> int:
        key = (x,y,k)
        if apples[y][x] == 0:
            return 0
        if k == 0:
            return 1
        
        key = (x,y,k)
        if key in memo:
            return memo[key]
        
        ans = 0
        for i in range(x+1, cols):
            if apples[y][x] - apples[y][i] > 0:
                ans += self.cuts(i, y, rows, cols, k-1, memo, apples)
        
        for j in range(y+1, rows):
            if apples[y][x] - apples[j][x] > 0:
                ans += self.cuts(x, j, rows, cols, k-1, memo, apples)

        memo[key] = ans

        return ans

    def ways(self, pizza: list[str], k: int) -> int:

        rows = len(pizza)
        cols = len(pizza[0])
        apples = [[0 for _ in range(cols + 1)] for _ in range(rows+1)]
        memo = {}
                
        for j in range(rows-1, -1, -1):
            for i in range(cols-1, -1, -1):
                apples[j][i] = int(pizza[j][i] == 'A') + apples[j+1][i] + apples[j][i+1] - apples[j+1][i+1]


        return self.cuts(0, 0, rows, cols, k-1, memo, apples) % int(1000000007)
    
class Solution:
    def ways(self, pizza: list[str], k: int) -> int:

        cols = len(pizza[0])
        rows = len(pizza)

        apples = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        dp = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(k)]

        for j in range(cols - 1, -1, -1):
            for i in range(rows - 1, -1, -1):
                apples[i][j] = int(pizza[i][j] == "A") + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
                dp[0][i][j] = int(apples[i][j] > 0)
        
        mod = 1000000007
        

        for remain in range(1, k):
            for i in range(0, rows):
                for j in range(0, cols):
                    val = 0
                    for next_i in range(i+1, rows):
                        if apples[i][j] - apples[next_i][j] > 0:
                            val+= dp[remain-1][next_i][j]
                    for next_j in range(j+1, cols):
                        if apples[i][j] - apples[i][next_j] > 0:
                            val += dp[remain-1][i][next_j]
                    dp[remain][i][j] = val % mod
        return dp[k-1][0][0]
    


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:

        cols = len(pizza[0])
        rows = len(pizza)

        apples = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for j in range(cols - 1, -1, -1):
            for i in range(rows - 1, -1, -1):
                apples[i][j] = int(pizza[i][j] == "A") + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
                dp[i][j] = int(apples[i][j] > 0)

        
        mod = 1000000007
        

        for _ in range(1, k):
            temp = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(0, rows):
                for j in range(0, cols):
                    val = 0
                    for next_i in range(i+1, rows):
                        if apples[i][j] - apples[next_i][j] > 0:
                            val+= dp[next_i][j]
                    for next_j in range(j+1, cols):
                        if apples[i][j] - apples[i][next_j] > 0:
                            val += dp[i][next_j]
                    temp[i][j] = val % mod
            dp = temp
        return dp[0][0]


        

        
                

