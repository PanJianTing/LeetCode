class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        ROW = len(image)
        COL = len(image[0])
        
        minX = ROW
        maxX = 0

        minY = COL
        maxY = 0

        for r in range(ROW):
            for c in range(COL):
                if image[r][c] == '1':
                    minX = min(minX, r)
                    maxX = max(maxX, r)
                    minY = min(minY, c)
                    maxY = max(maxY, c)
        
        return (maxX - minX + 1) * (maxY - minY + 1)
    


print(Solution().minArea([["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], 0, 2))