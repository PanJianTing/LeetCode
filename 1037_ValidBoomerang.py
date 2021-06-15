class Solution:

    # 用斜率 (p3y-p2y) / (p3x-p2x) = (p2y-p1y) / (p2x/p1x)
    # 推得 => (p3y-p2y) * (p2x/p1x) = (p3x-p2x) * (p2y-p1y)

    def isBoomerang(self, points: list[int]) -> bool:
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        return ((p3[1] - p2[1]) * (p2[0] - p1[0])) != ((p2[1] - p1[1]) * (p3[0] - p2[0]))

    def isBoomerang_my(self, points: list[int]) -> bool:

        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        if p1 == p2 or p2 == p3 or p1 == p3:
            return False

        if (p2[0] - p1[0]) == 0:
            s1 = -99999999999
        else:
            s1 = (p2[1] - p1[1]) / (p2[0] - p1[0])

        if (p3[0] - p2[0]) == 0:
            s2 = -99999999999
        else:
            s2 = (p3[1] - p2[1]) / (p3[0] - p2[0])

        return not(s1 == s2)


Solution.isBoomerang(Solution(), [[0,1],[0,2],[1,2]])