from functools import cache

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        N = len(days)

        @cache
        def dp(cur_idx, cur_expired):
            if cur_idx == N:
                return 0
            
            if days[cur_idx] <= cur_expired:
                return dp(cur_idx+1, cur_expired)

            cur_day = days[cur_idx]
            min_cost = costs[0] + dp(cur_idx+1, cur_day)
            min_cost = min(min_cost, costs[1] + dp(cur_idx+1, cur_day+6))
            min_cost = min(min_cost, costs[2] + dp(cur_idx+1, cur_day+29))

            return min_cost

        return dp(0, 0)
    

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        day_set = set(days)
        dp = [float('inf')] * 366
        dp[0] = 0

        for i in range(1, 366):
            if i in day_set:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[365]

    


# print(Solution().mincostTickets([1,4,6,20], [2,7,15]))
# print(Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]))
print(Solution().mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28], [3,13,45]))