class Solution:
    def countNegatives(self, G: list[list[int]]) -> int:
        M = len(G)
        N = len(G[0])

        res = 0

        for i in range(M):
            for j in range(N):
                if G[i][j] < 0:
                    res += 1

        return res
    
    def countNegatives(self, G: list[list[int]]) -> int:
        M = len(G)
        N = len(G[0])

        res = 0
        
        for i in range(M):
            
            if G[i][0] < 0:
                res += (M - i) * N
                break

            for j in range(N):
                if G[i][j] < 0:
                    res += N - j
                    break
            
        return res
    
    def countNegatives(self, G: list[list[int]]) -> int:
        M = len(G)
        N = len(G[0])

        res = 0

        for i in range(M):
            
            l = 0
            r = N-1
            while l <= r:
                m = (r-l) >> 1
                if G[i][m] < 0:
                    r = m - 1
                else:
                    l = m+1
            res +=  N - l
        return res
    
    def countNegatives(self, G: list[list[int]]) -> int:
        M = len(G)
        N = len(G[0])

        idx = N - 1
        res = 0

        for row in G:
            while idx >= 0 and row[idx] < 0:
                idx -= 1

            res += N - (idx+1)
        return res
            

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
