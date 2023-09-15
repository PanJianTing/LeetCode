class Solution:
    def candy(self, ratings):
        N = len(ratings)
        candyList = [0] * N
        candyList[0] = 1

        for i in range(1, N):
            now = ratings[i]
            before = ratings[i-1]
            if now > before:
                candyList[i] = candyList[i-1] + 1
            elif now == before:
                candyList[i] = 1
            else:
                candyList[i] = 1
                j = i
                while j > -1 and ratings[j-1] > ratings[j] and candyList[j-1] <= candyList[j]:
                    candyList[j-1] += 1
                    j -= 1

        return sum(candyList)
    
    def candy(self, ratings):
        N = len(ratings)
        allCandy = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                allCandy[i] = allCandy[i-1]+1
        
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                allCandy[i] = max(allCandy[i], allCandy[i+1]+1)

        return sum(allCandy)
    
print(Solution().candy([1,0,2]))
print(Solution().candy([1,2,2]))
print(Solution().candy([1,3,2,2,1]))