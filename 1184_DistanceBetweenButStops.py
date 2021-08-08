class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:

        if start > destination:
            start, destination = destination, start
        
        # 順時針
        totalDis = sum(distance[start:destination])
        # 逆時針
        totalDis_r = sum(distance[0:start]) + sum(distance[destination:])


        return min(totalDis, totalDis_r)



    def distanceBetweenBusStops_my(self, distance: list[int], start: int, destination: int) -> int:

        countStop = len(distance)

        totalDis = 0

        totalDis_r = 0
        srart_r = start
        
        while start != destination:
            totalDis += distance[start]

            if start + 1 >= countStop:
                start = 0
            else:
                start += 1
            

        while srart_r != destination:
            if srart_r - 1 < 0:
                srart_r = countStop - 1
            else:
                srart_r -= 1

            totalDis_r += distance[srart_r]


        return min(totalDis, totalDis_r)

# Solution.distanceBetweenBusStops(Solution(), [1,2,3,4], 0, 3)

# Solution.distanceBetweenBusStops(Solution(), [8,11,6,7,10,11,2], 0, 3)

Solution.distanceBetweenBusStops(Solution(), [7,10,1,12,11,14,5,0], 7, 2)