from collections import Counter

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        mx = 0
        for i, (x0, y0) in enumerate(points[:-1]):
            cnt = Counter(((x-x0)/(y-y0) if (y-y0) != 0 else None) for x, y in points[i+1:])
            print(cnt)
            print(cnt.values())
            mx = max(mx, max(cnt.values()))
        return mx+1


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        res = 0

        for i in range(0, len(points)):
            resultMap = {}
            sameX = {}
            sameY = {}
            for j in range(i+1 , len(points)):
                xj, yj = points[j][0], points[j][1]
                xi, yi = points[i][0], points[i][1]
                # print("j : ( {} , {} ), i : ( {}, {} )".format(xj, yj , xi, yi))

                if xi == xj:
                    if xi in sameX:
                        sameX[xi].add(i)
                        sameX[xi].add(j)
                    else:
                        sameX[xi] = set((i, j))
                    
                    continue
                elif yi == yj:
                    if yi in sameY:
                        sameY[yi].add(i)
                        sameY[yi].add(j)
                    else:
                        sameY[yi] = set((i, j))

                    continue
                else:
                    m = (yj - yi) / (xj - xi)

                # print(m)

                if m in resultMap:
                    resultMap[m].add(i)
                    resultMap[m].add(j)
                else:
                    resultMap[m] = set((i, j))

            resultCount = 0
            for key in resultMap.keys():
                if len(resultMap[key]) > resultCount:
                    resultCount = len(resultMap[key])

            for key in sameX.keys():
                if len(sameX[key]) > resultCount:
                    resultCount = len(sameX[key])

            for key in sameY.keys():
                if len(sameY[key]) > resultCount:
                    resultCount = len(sameY[key])

            if resultCount > res:
                res = resultCount

        return res
            

# Solution().maxPoints([[1,1],[2,2],[3,3]])

# Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])

Solution().maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]])
