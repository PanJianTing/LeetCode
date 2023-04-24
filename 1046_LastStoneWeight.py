import heapq
import bisect

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
    

class Solution:

    def lastStoneWeight(self, stones: list[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, (heapq.heappop(h)-heapq.heappop(h)))
        return -h[0]
    
    def lastStoneWeight(self, A:list[int]) -> int:
        A.sort()
        while len(A) > 1:
            bisect.insort(A, A.pop() - A.pop())
        return A[0]
        
            


    def lastStoneWeight(self, stones: list[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1
    
        heapq.heapify(stones)

        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        
        return -stones[0]

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones.sort()
        while (len(stones) > 1):
            x = stones.pop()
            y = stones.pop()
            if abs(x-y):
                stones.append(abs(x-y))
                stones.sort()
        return stones[0] if len(stones) else 0
    
class Solution:
    def lastStoneWeight(self, A: list[int]) -> int:

        def removeLargest():
            index = A.index(max(A))
            A[index], A[-1] = A[-1], A[index]
            return A.pop()
        
        while len(A) > 1:
            A.append(removeLargest() - removeLargest())
        return A[0]
    

class Solution:
    def lastStoneWeight(self, A: list[int]) -> int:

        max_weight = max(A)
        buckets = [0] * (max_weight + 1)

        for w in A:
            buckets[w] += 1

        biggest_w = 0
        curr = max_weight
        while curr > 0:
            if buckets[curr] == 0:
                curr -= 1
            elif biggest_w == 0:
                buckets[curr] %= 2
                if buckets[curr] == 1:
                    biggest_w = curr
                curr -= 1
            else:
                buckets[curr] -= 1
                if biggest_w - curr <= curr:
                    buckets[biggest_w - curr] += 1
                    biggest_w = 0
                else:
                    biggest_w -= curr

        return biggest_w

print(Solution.lastStoneWeight(Solution(), [2,7,4,1,8,1]))
print(Solution.lastStoneWeight(Solution(), [1,3]))
print("Hello world")