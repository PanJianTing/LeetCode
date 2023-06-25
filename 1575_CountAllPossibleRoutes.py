from functools import cache

class Solution:

    # Sol #1 top-down
    def countRoutes(self, location, start, finish, fuel) -> int:

        N = len(location)
        
        @cache
        def dp(curr, currFuel):
            if currFuel < 0:
                return 0
            ans = 0
            if curr == finish:
                ans += 1
            
            for i in range(N):
                if curr == i:
                    continue
                nextF = currFuel - (abs(location[i] - location[curr]))
                ans += dp(i, nextF)

            return ans
        
        return dp(start, fuel) % (10 ** 9 + 7)
    
    # Sol #2 bottom-up
    def countRoutes(self, location, start, finish, fuel) -> int:

        N = len(location)
        dp = [[0] * (fuel+1) for _ in range(N)]
        for i in range(fuel+1):
            dp[finish][i] = 1

        for f in range(fuel+1):
            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    if abs(location[i] - location[j]) <= f:
                        dp[i][f] += dp[j][f - abs(location[i] - location[j])]

        return dp[start][fuel] % (10**9+7)
    
    def countRoutes(self, location, start, finish, fuel) -> int:

        N = len(location)
        dp = [[0] * (fuel+1) for _ in range(N)]

        dp[start][fuel] = 1

        for f in range(fuel, -1, -1):
            for i in range(N):
                if dp[i][f] == 0:
                    continue
                for j in range(N):
                    if i == j:
                        continue
                    cost = abs(location[i] - location[j])
                    if cost <= f:
                        dp[j][f-cost] += dp[i][f]

        ans = 0
        for i in range(fuel+1):
            ans += dp[finish][i]

        return ans % (10**9+7)
    

    def countRoutes(self, location, start, finish, fuel) -> int:
        N = len(location)
        
        @cache
        def dp(curr, currFuel):

            if currFuel < 0:
                return 0

            if curr == finish:
                return 1
            
            count = 0
            for i in range(N):
                if curr != i:
                    cost = abs(location[i] - location[curr])
                    count += dp(i, currFuel - cost)
                    # if cost <= currFuel:
                        

            return count

        return dp(start, fuel) % (10**9+7)


print(Solution().countRoutes([2,3,6,8,4], 1, 3, 5))