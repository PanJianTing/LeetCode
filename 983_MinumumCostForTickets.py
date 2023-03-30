class Solution:
    memo = {}

    def dp(self, day: int, days: list[int], cost: list[int]) -> int:
        if day > days[-1]:
            return 0

        if day in self.memo:
            return self.memo[day]

        ans = 0
        if day in days:
            ans = min(self.dp(day+1, days, cost) + cost[0], self.dp(day+7, days, cost) + cost[1], self.dp(day+30, days, cost) + cost[2])
        else:
            ans = self.dp(day+1, days, cost)
        
        self.memo[day] = ans
        return ans

    
    def mincostTickets(self, days: list[int], cost: list[int]) -> int:

        self.memo = {}
        return self.dp(1, days, cost)
    
class Solution:
    memo = {}

    def dp(self, index: int, days: list[int], cost: list[int]) -> int:
        if index >= len(days):
            return 0
        if index in self.memo:
            return self.memo[index]
        
        duration = [1,7,30]
        ans = 999999999
        j = index

        for d, c in zip(duration, cost):
            while j < len(days) and days[j] < days[index] + d:
                j += 1
            ans = min(ans, self.dp(j, days, cost) + c) 
        self.memo[index] = ans
        return ans

    
    def mincostTickets(self, days: list[int], cost: list[int]) -> int:

        self.memo = {}
        return self.dp(0 ,days, cost)
    
class Solution:
    def mincostTickets(self, days: list[int], cost: list[int]) -> int:

        dp = [0 for _ in range(days[-1] + 1)]

        for i in range(days[-1] + 1):

            if i in days:
                dp[i] = min(dp[max(0, i-1)]+ cost[0], dp[max(0, i-7)]+ cost[1], dp[max(0, i-30)]+ cost[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]

