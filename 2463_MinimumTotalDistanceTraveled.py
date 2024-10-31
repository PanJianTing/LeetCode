from functools import cache

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        M = len(robot)
        N = len(factory)
        factory_pos = []
        robot.sort()
        factory.sort(key=lambda x: x[0])
        

        for pos, limit in factory:
            for _ in range(limit):
                factory_pos.append(pos)

        N = len(factory_pos)


        @cache
        def dp(robot_idx, factory_idx):
            if robot_idx == M:
                return 0
            if factory_idx == N:
                return float('inf')
            
            res1 = abs(robot[robot_idx] - factory_pos[factory_idx]) + dp(robot_idx+1, factory_idx+1)
            res2 = dp(robot_idx, factory_idx + 1)

            return min(res1, res2)

        return dp(0, 0)
    

    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        M = len(robot)
        N = len(factory)
        factory_pos = []
        robot.sort()
        factory.sort(key=lambda x: x[0])
        

        for pos, limit in factory:
            for _ in range(limit):
                factory_pos.append(pos)

        N = len(factory_pos)


        dp_table = [[None] * (N+1) for _ in range(M+1)]
        
        def dp(robot_idx, factory_idx):
            if dp_table[robot_idx][factory_idx]:
                return dp_table[robot_idx][factory_idx]
            
            if robot_idx == M:
                dp_table[robot_idx][factory_idx] = 0
                return 0
            if factory_idx == N:
                dp_table[robot_idx][factory_idx] = float('inf')
                return float('inf')
            
            res1 = abs(robot[robot_idx] - factory_pos[factory_idx]) + dp(robot_idx+1, factory_idx+1)
            res2 = dp(robot_idx, factory_idx + 1)

            dp_table[robot_idx][factory_idx] = min(res1, res2)

            return dp_table[robot_idx][factory_idx]

        return dp(0, 0)
    

    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()

        factory_pos = []

        for pos, cnt in factory:
            for _ in range(cnt):
                factory_pos.append(pos)
        
        M = len(robot)
        N = len(factory_pos)

        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            dp[i][N] = float('inf')

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                res1 = abs(robot[i] - factory_pos[j]) + dp[i+1][j+1]
                res2 = dp[i][j+1]
                dp[i][j] = min(res1, res2)

        return dp[0][0]

print(Solution().minimumTotalDistance([0,4,6], [[2,2],[6,2]]))
print(Solution().minimumTotalDistance([1,-1], [[-2,1],[2,1]]))
print(Solution().minimumTotalDistance([9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]))