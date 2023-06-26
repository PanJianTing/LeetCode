import heapq

class Solution:

    # Solution #1 two priority queue
    def totalCost(self, costs, k, candidates) -> int:

        res = 0
        left = []
        right = []
        for _ in range(candidates):
            if len(costs):
                heapq.heappush(left, costs.pop(0))
            if len(costs):
                heapq.heappush(right, costs.pop())

        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                res += heapq.heappop(left)
                if len(costs):
                    heapq.heappush(left, costs.pop(0))
            else:
                res += heapq.heappop(right)
                if len(costs):
                    heapq.heappush(right, costs.pop())
        return res
    
    # Sol #2 two priority queue and two points
    def totalCostr(self, costs, k, candidates) -> int:

        res = 0
        N = len(costs)
        left = costs[:candidates]
        right = costs[max(candidates, N - candidates):]
        leftIdx = candidates
        rightIdx = N - 1 - candidates 

        heapq.heapify(left)
        heapq.heapify(right)
        
        for _ in range(k):
            
            # 先看右邊有沒有值 如果有值 在看左邊是否有值 且 左邊[0]小於右邊[0]
            if (not right) or (left and (left[0] <= right[0])):
                res += heapq.heappop(left)

                if leftIdx <= rightIdx:
                    heapq.heappush(left, costs[leftIdx])
                    leftIdx += 1
            else:
                res += heapq.heappop(right)
                
                if leftIdx <= rightIdx:
                    heapq.heappush(right, costs[rightIdx])
                    rightIdx -= 1
                
        return res
    
    # Sol #3 one priority queue and two points
    def totalCostr(self, costs, k, candidates) -> int:

        res = 0
        N = len(costs)
        hq = []
        for i in range(candidates):
            hq.append((costs[i], 0))
            # heapq.heappush(hq, (costs[i], 0))
        for i in range(max(candidates, N - candidates), N):
            hq.append((costs[i], 1))
            # heapq.heappush(hq, (costs[i], 1))
        
        heapq.heapify(hq)
        leftIdx = candidates
        rightIdx = N - 1 - candidates 

        
        for _ in range(k):
            c, s = heapq.heappop(hq)
            res += c

            if leftIdx <= rightIdx:
                if s:
                    heapq.heappush(hq, (costs[rightIdx], s))
                    rightIdx -= 1
                else:
                    heapq.heappush(hq, (costs[leftIdx], s))
                    leftIdx += 1

        return res
    


print(Solution().totalCost([17,12,10,2,7,2,11,20,8], 3, 4)) #11
print(Solution().totalCost([1,2,4,1], 3, 3)) #4
print(Solution().totalCost([57,33,26,76,14,67,24,90,72,37,30], 11, 2)) #526
print(Solution().totalCost([18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], 13, 23)) #223
print(Solution().totalCost([48], 1, 1)) #48
print(Solution().totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2)) #423


