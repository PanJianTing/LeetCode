class Solution:
    def maxDistance(self, pos: list[int], m: int) -> int:
        N = len(pos)
        ans = 0
        pos.sort()
        l = 1
        r = (pos[-1] - pos[0]) // (m-1)

        def canDistance(cur):
            pre_pos = pos[0]
            ballPlaced = 1

            for i in range(1, N):
                cur_pos = pos[i]
                
                if cur_pos - pre_pos >= cur:
                    ballPlaced += 1
                    pre_pos = cur_pos

                if ballPlaced == m:
                    return True
            
            return False
        
        while l <= r:
            mid = l + ((r-l) >> 1)

            if canDistance(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
    
print(Solution().maxDistance([1,2,3,4,7], 3))
print(Solution().maxDistance([5,4,3,2,1,1000000000], 2))