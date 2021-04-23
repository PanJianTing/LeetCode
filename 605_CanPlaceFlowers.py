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

print("Hello World!")