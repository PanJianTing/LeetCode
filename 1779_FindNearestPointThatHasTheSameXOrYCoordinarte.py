class Solution:

    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:

        return min(((abs(a-x)+abs(b-y),i) for i,(a,b) in enumerate(points) if a == x or b == y), default=(0, -1))[1]


    def nearestValidPoint_1(self, x: int, y: int, points: list[list[int]]) -> int:

        nearestDis = 9999999
        smallIndex = -1

        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dis = abs(x-point[0]) + abs(y-point[1])
                if nearestDis > dis:
                    nearestDis = dis
                    smallIndex = i
        return smallIndex


    def nearestValidPoint_my(self, x: int, y: int, points: list[list[int]]) -> int:

        validPointMap = {}
        nearestDis = 999999999

        for i in range(0, len(points)):
            point = points[i]
            if point[0] == x:
                validPointMap[i] = point
            elif point[1] == y:
                validPointMap[i] = point
        
        for i, key in enumerate(validPointMap):
            point = validPointMap[key]
            dis = abs(point[0] - x) + abs(point[1] - y)
            if nearestDis > dis:
                nearestDis = dis
        
        for i, key in enumerate(validPointMap):
            point = validPointMap[key]
            dis = abs(point[0] - x) + abs(point[1] - y)
            if nearestDis == dis:
                return key
        return -1


Solution.nearestValidPoint(Solution(), 3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])