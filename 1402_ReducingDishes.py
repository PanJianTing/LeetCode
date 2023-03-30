class Solution:

    def dp(self, index: int, time: int, sat: list[int], memo: dict) -> int:

        if index >= len(sat):
            return 0
        
        if (index, time) in memo:
            return memo[(index, time)]
        
        maxDish = max(self.dp(index + 1, time, sat, memo), sat[index] * time + self.dp(index+1, time + 1, sat, memo))

        memo[(index, time)] = maxDish
        return maxDish

    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        dp = [0 for _ in range(0, len(satisfaction))]

        satisfaction.sort()

        return self.dp(0, 1, satisfaction, dict())
    

    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        dp = [[0 for _ in range(0, len(satisfaction) + 2)] for _ in range(0, len(satisfaction) + 1)]
        satisfaction.sort()

        for dish in range(len(satisfaction)-1, -1, -1):
            for time in range(1, len(satisfaction) + 1):

                dp[dish][time] = max(satisfaction[dish] * time + dp[dish+1][time+1], dp[dish+1][time])

        return dp[0][1]
    
    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        preTime = [0 for _ in range(0, len(satisfaction) + 2)]

        satisfaction.sort()

        for dish in range(len(satisfaction)-1, -1, -1):
            
            nowTime = [0 for _ in range(0, len(satisfaction) + 2)]

            for time in range(1, len(satisfaction)+1):
                
                nowTime[time] = max(satisfaction[dish] * time + preTime[time+1], preTime[time])

            preTime = nowTime

        return preTime[1]
    
    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        satisfaction.sort()
        suffixSum = 0
        maxCoefficient = 0

        for i in range(len(satisfaction)-1, -1, -1):
            suffixSum += satisfaction[i]
            if suffixSum >= 0:
                maxCoefficient += suffixSum

        return maxCoefficient
        
