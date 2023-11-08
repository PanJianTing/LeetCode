class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t) -> bool:
        if sx == fx and sy == fy:
            if t >= 0:
                return True

        if t <= 0:
            if sx == fx and sy == fy:
                return True
            else:
                return False
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1, 1), (1, -1), (1, 1)]
        
        for dx, dy in directions:
            if self.isReachableAtTime(sx+dx, sy+dy, fx, fy, t-1):
                return True
            
        return False
    
    def isReachableAtTime(self, sx, sy, fx, fy, t) -> bool:
        w = abs(fx - sx)
        h = abs(fy - sy)

        if w == 0 and h == 0 and t == 1:
            return False
        return t >= max(w, h)

print(Solution().isReachableAtTime(2,4,7,7,6))     
print(Solution().isReachableAtTime(3,1,7,3,3))     
print(Solution().isReachableAtTime(1,1,3,3,9))     