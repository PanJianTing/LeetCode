class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        temp_red = red
        temp_blue = blue

        h1 = 0
        curColor = 0
        while 1:
            if curColor:
                if temp_blue >= (h1+1):
                    h1+=1
                    temp_blue -= h1
                    curColor = 0
                else:
                    break
            else:
                if temp_red >= (h1 + 1):
                    h1 += 1
                    temp_red -= h1
                    curColor = 1
                else:
                    break

        temp_red = red
        temp_blue = blue

        h2 = 0
        curColor = 0

        while 1:
            if curColor:
                if temp_red >= (h2+1):
                    h2+=1
                    temp_red -= h2
                    curColor = 0
                else:
                    break
            else:
                if temp_blue >= (h2+1):
                    h2 += 1
                    temp_blue -= h2
                    curColor = 1
                else:
                    break

        return max(h1, h2)
    


    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def getHeight(cnt):
            h = 0
            cur = 0
            while cnt[cur] >= (h+1):
                h += 1
                cnt[cur] -= h
                cur = (not cur)
            return h
        return max(getHeight([red, blue]), getHeight([blue, red]))

    
print(Solution().maxHeightOfTriangle(2, 4))
print(Solution().maxHeightOfTriangle(2, 1))
print(Solution().maxHeightOfTriangle(1, 1))
print(Solution().maxHeightOfTriangle(10, 1))
    
    
        

        