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
    

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        N = len(coordinates)
        A = coordinates[0]
        B = coordinates[1]

        isHor = False


        if (B[0] - A[0]) == 0:
            isHor = True
        else:
            base = (B[1] - A[1]) / (B[0] - A[0])

        for i in range(2, N):
            B = coordinates[i]
            A = coordinates[i-1]
            if isHor and B[0] != A[0]:
                return False
            else:
                if isHor:
                    continue
                if B[0] - A[0] == 0:
                    L = (B[1] - A[1]) 
                else:
                    L = (B[1] - A[1]) / (B[0] - A[0])
                if L != base:
                    return False
        return True
    
    def checkStraightLine(self, C: list[list[int]]) -> bool:

        if all(x == C[0][0] for x, y in C):
            return True
        
        N = len(C)
        A = C[0]
        B = C[1]

        if B[0] - A[0] == 0:
            return False
        
        base = (B[1] - A[1]) / (B[0] - A[0])

        for i in range(2, N):
            B = C[i]
            A = C[i-1]

            if B[0] - A[0] == 0:
                return False
            else:
                L = (B[1] - A[1]) / (B[0] - A[0])
                if (base == L) == False:
                    return False
                
        return True
    
    def checkStraightLine(self, C: list[list[int]]) -> bool:

        if all(x == C[0][0] for x, y in C):
            return True
        
        x1, y1 = C[0]
        x2, y2= C[1]

        if (x2 - x1) == 0:
            return False
        
        m = (y2 - y1) / (x2 - x1)
        '''
        y2 = m(x2 - x1) + y1
        y2 = m * x2 - m * x1 + y1
        y2 = m * x2 + (-m * x1 + y1)
                            b
        '''
        b = -(m * x1) + y1
        for c in C:
            if c[1] != m * c[0] + b:
                return False
        return True
    
    '''
    if c0(x0, y0), c1(x1, y1), c2(x2, y2) is Line, then
    
     y1 - y0     y2 - y0
    --------- = --------- => (y1 - y0) * (x2 - x0) = (y2 - y0) * (x1 - x0)
     x1 - x0     x2 - x0

    '''
    def checkStraightLine(self, C: list[list[int]]) -> bool:

        x0, y0 = C[0]
        x1, y1 = C[1]
        dX = x1 - x0
        dY = y1 - y0
        N = len(C)

        for i in range(2, N):
            x2, y2 = C[i]

            if (dY * (x2 - x0)) != ((y2 - y0) * dX):
                return False
        return True


Solution.checkStraightLine(Solution(), [[1,-8],[2,-3],[1,2]])