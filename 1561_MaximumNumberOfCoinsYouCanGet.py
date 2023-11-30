from collections import deque

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        pickCnt = len(piles) // 3

        piles = sorted(piles, reverse=True)
        ans = 0
        idx = 1
        while pickCnt != 0:
            ans += piles[idx]
            idx += 2
            pickCnt -= 1

        return ans
    

    def maxCoins(self, piles: list[int]) -> int:
        N = len(piles)
        piles.sort()
        ans = 0
        for i in range(N // 3, N, 2):
            ans += piles[i]

        return ans
    
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        q = deque(piles)
        N = len(piles)
        ans = 0

        while q:
            q.pop()
            ans += q.pop()
            q.popleft()
            
        return ans
    
    def maxCoins(self, piles) -> int:
        return sum(sorted(piles)[(len(piles) // 3)::2])
            
    
print(Solution().maxCoins([2,4,1,2,7,8]))
print(Solution().maxCoins([2,4,5]))
print(Solution().maxCoins([9,8,7,6,5,1,2,3,4]))
