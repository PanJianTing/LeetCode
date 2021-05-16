class Solution:

    def slope(self, c1: list[int], c2: list[int]) -> int:
        
        x = c2[0] - c1[0]
        y = c2[1] - c1[1]

        if x == 0:
            return -1
        else:
            return y / x


    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        m = self.slope(coordinates[1], coordinates[0])

        for i in range(2, len(coordinates)):
            if self.slope(coordinates[i], coordinates[i-1]) != m:
                return False

        return True



    def checkStraightLine_my(self, coordinates: list[list[int]]) -> bool:

        setZ = set()

        for i in range(1, len(coordinates)):

            nowX = coordinates[i][0] - coordinates[i-1][0]
            nowY = coordinates[i][1] - coordinates[i-1][1]
            
            if nowX == 0:
                setZ.add(-1)
            else:
                setZ.add(nowY / nowX)
                
        return len(setZ) == 1


Solution.checkStraightLine(Solution(), [[1,-8],[2,-3],[1,2]])