
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        stones.sort()

        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if x != y:
                weight = x - y
                stones.append(weight)
                stones.sort()
                
                
        if len(stones) > 0:
            return stones[0]


        return 0

print(Solution.lastStoneWeight(Solution(), [2,7,4,1,8,1]))
print(Solution.lastStoneWeight(Solution(), [1,3]))
print("Hello world")