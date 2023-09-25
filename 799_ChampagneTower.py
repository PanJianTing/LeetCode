class Solution:
    def champagneTower(self, poured, row, glass):
        tower = [[0] * 100 for _ in range(100)]
        tower[0][0] = 1.0
        fullglass = set()
        fullglass.add((0,0))

        for _ in range(1, poured):
            temp = set(fullglass)
            for r, idx in temp:
                add = 1 / pow(2, r+1)
                if tower[r+1][idx] < 1.0:
                    tower[r+1][idx] += add

                if tower[r+1][idx+1] < 1.0:
                    tower[r+1][idx+1] += add

                if tower[r+1][idx] >= 1.0:
                    fullglass.add((r+1, idx))

                if tower[r+1][idx+1] >= 1.0:
                    fullglass.add((r+1, idx+1))

        return tower[row][glass]
    

    def champagneTower(self, poured, row, glass):
        tower = [[0] * 101 for _ in range(101)]
        tower[0][0] = poured
        for i in range(0, row+1):
            for j in range(0, i+1):
                q = (tower[i][j] - 1) / 2
                if q > 0:
                    tower[i+1][j] += q
                    tower[i+1][j+1] += q
        
        return min(1.0, tower[row][glass])

    

# print(Solution().champagneTower(1,1,1))
# print(Solution().champagneTower(2,1,1))
print(Solution().champagneTower(8,1,1))
print(Solution().champagneTower(1000000000, 99, 99))


                