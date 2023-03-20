class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        canAdd = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] ==0):
                flowerbed[i] = 1
                canAdd += 1
                
        return n > canAdd == False
    
    def canPlaceFlowers_my(self, flowerbed: list[int], n: int) -> bool:
        canAdd = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                canAdd += 1
        else:
            for i in range(0, len(flowerbed)):

                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            canAdd += 1
                    elif i == len(flowerbed) - 1:
                        if flowerbed[i-1] == 0:
                            flowerbed[i] = 1
                            canAdd += 1
                    else:
                        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            canAdd += 1
                        
        if n > canAdd:
            return False
        return True
    

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        m = len(flowerbed)

        for i, plot in enumerate(flowerbed):
            if plot == 0:
                isCan = True
                if i-1 > -1:
                    if flowerbed[i-1] == 1:
                        isCan = False
                if i+1 < m:
                    if flowerbed[i+1] == 1:
                        isCan = False
                if isCan:
                    flowerbed[i] = 1
                    n -= 1
        if n > 0:
            return False
        return True
    
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        m = len(flowerbed)
        plots = 0

        for i, plot in enumerate(flowerbed):

            if plot == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == m-1) or (flowerbed[i+1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    plots += 1

                    if plots >= n:
                        return True
                    
        return plots >= n
