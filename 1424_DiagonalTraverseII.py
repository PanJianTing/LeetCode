from collections import defaultdict
from collections import deque
import heapq

class Solution:
    # TLE
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        M = len(nums)
        N = 0
        ans = []
        for i in range(M):
            N = max(N, len(nums[i]))

        total = M+N-1
        cur = 0
        for cur in range(total):
            cur_i = cur
            cur_j = 0
            while cur_i >= 0:
                if cur_i < M and cur_j < len(nums[cur_i]):
                    ans.append(nums[cur_i][cur_j])
                cur_i -= 1
                cur_j += 1
            
        return ans
    
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        
        q = []
        ans = []
        M = len(nums)

        for i in range(M):
            for j in range(len(nums[i])):
                heapq.heappush(q, (i+j, -i, nums[i][j]))
        
        while q:
            _, _, n = heapq.heappop(q)
            ans.append(n)
        
        return ans
    
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        group_map = defaultdict(list)
        ans = []
        max_key = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])):
                group_map[i+j].append(nums[i][j])
                max_key = max(max_key, i+j)

        for cur in range(max_key+1):
            ans.extend(group_map[cur])

        while cur in group_map:
            ans.extend(group_map[cur])
            cur += 1

        return ans
    
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        group_map = defaultdict(list)
        ans = []
        cur = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])):
                group_map[i+j].append(nums[i][j])

        while cur in group_map:
            ans.extend(group_map[cur])
            cur += 1

        return ans
    
    def findDiagonalOrder(self, nums) -> list[int]:
        ans = []
        q = deque()
        q.append((0, 0))
        M = len(nums)

        while q:
            i, j = q.popleft()
            ans.append(nums[i][j])

            if j == 0 and i+1 < M:
                q.append((i+1, j))
            if j + 1 < len(nums[i]):
                q.append((i, j+1))
        return ans

    
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
