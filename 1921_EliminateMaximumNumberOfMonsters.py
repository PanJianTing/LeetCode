import heapq

class Solution:
    def eliminateMaximum(self, dist, speed) -> int:
        q = []
        N = len(dist)
        ans = 0

        for i in range(N):
            heapq.heappush(q, dist[i] / speed[i])

        while q:
            time = heapq.heappop(q)
            if time <= ans:
                return ans
            
            ans += 1
        return ans
    
    
    def eliminateMaximums(self, dist, speed) -> int:
        arrival = []
        N = len(dist)
        
        for i in range(N):
            arrival.append(dist[i] / speed[i])

        arrival.sort()
        ans = 0

        for idx, time in enumerate(arrival):
            if  time <= idx:
                return ans
            ans += 1
        return N
    
    
print(Solution().eliminateMaximum([1,3,4], [1,1,1]))
print(Solution().eliminateMaximum([1,1,2,3], [1,1,1,1]))
print(Solution().eliminateMaximum([3,2,4], [5,3,2]))
print(Solution().eliminateMaximum([4,2,8], [2,1,4]))
print(Solution().eliminateMaximum([4,2,3], [2,1,1]))
        