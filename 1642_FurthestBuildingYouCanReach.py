from functools import cache
import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)

        @cache
        def dp(cur, remain_b, remain_l):
            if cur == N-1:
                return cur
            if heights[cur] >= heights[cur+1]:
                return dp(cur+1, remain_b, remain_l)
            
            need_brick = heights[cur+1] - heights[cur]
            ans = cur
            if remain_b >= need_brick:
                ans = max(ans, dp(cur+1, remain_b-need_brick, remain_l))
            if remain_l > 0:
                ans = max(ans, dp(cur+1, remain_b, remain_l-1))
            
            return ans
        return dp(0, bricks, ladders)
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        ans = 0
        hp = [(0, bricks, ladders)]

        while hp:
            cur, remain_b, remain_l = heapq.heappop(hp)
            cur *= -1
            if cur == N-1:
                return cur
            if heights[cur] >= heights[cur+1]:
                heapq.heappush(hp, ((cur+1) * -1, remain_b, remain_l))
                continue

            need_brick = heights[cur+1] - heights[cur]
            if need_brick > remain_b and remain_l <= 0:
                ans = max(ans, cur)
                continue
            
            if remain_b >= need_brick:
                heapq.heappush(hp, ((cur+1) * -1, remain_b - need_brick, remain_l))

            if remain_l > 0:
                heapq.heappush(hp, ((cur+1) * -1, remain_b, remain_l-1))
        return ans
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        cur_ladder = []
        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            if len(cur_ladder) < ladders:
                heapq.heappush(cur_ladder, diff)
            else:
                if cur_ladder and cur_ladder[0] < diff:
                    bricks -= heapq.heappop(cur_ladder)
                    heapq.heappush(cur_ladder, diff)
                else:
                    bricks -= diff
                if bricks < 0:
                    return i
        return N-1
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        cur_ladder = []
        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(cur_ladder, diff)
            if len(cur_ladder) <= ladders:
                continue
            bricks -= heapq.heappop(cur_ladder)
            if bricks < 0:
                return i
        return N-1
    
    def furthestBuilding(self, heights: list[int], bricks: int, laddars: int) -> int:
        N = len(heights)
        bricks_list = []

        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(bricks_list, (diff * -1))
            bricks -= diff
            if bricks < 0:
                bricks += -1 * heapq.heappop(bricks_list)
                laddars -= 1
                if laddars < 0:
                    return i
        return N-1
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        lo = 0
        hi = N-1

        def isReach(curIdx, b, l):
            diffs = []
            for i in range(curIdx):
                diff = heights[i+1] - heights[i]
                if diff > 0:
                    diffs.append(diff)
            diffs.sort()

            for d in diffs:
                if d <= b:
                    b -= d
                elif l > 0:
                    l -= 1
                else:
                    return False
            return True
        
        while lo < hi:
            mid = lo + ((hi - lo + 1) >> 1)

            if isReach(mid, bricks, ladders):
                lo = mid
            else:
                hi = mid - 1
        
        return lo
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        lo = 0
        hi = N-1
        diff_list = []

        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                diff_list.append((diff, i+1))

        diff_list.sort()

        def isReach(curIdx, b, l):
            for d, idx in diff_list:
                if idx > curIdx:
                    continue
                if d <= b:
                    b -= d
                elif l > 0:
                    l -= 1
                else:
                    return False
            return True
        
        while lo < hi:
            mid = lo + ((hi - lo + 1) >> 1)

            if isReach(mid, bricks, ladders):
                lo = mid
            else:
                hi = mid - 1
        
        return lo
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        hq = []

        for i in range(N-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(hq, diff)
            if len(hq) > ladders:
                bricks -= heapq.heappop(hq)
            if bricks < 0:
                return i
        return N-1
    
print(Solution().furthestBuilding([4,2,7,6,9,14,12], 5, 1))
print(Solution().furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))
print(Solution().furthestBuilding([14,3,19,3], 17, 0))
print(Solution().furthestBuilding([1,5,1,2,3,4,10000], 4, 1))

    

