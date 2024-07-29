from functools import cache

class Solution:

    # TLE
    def numTeams(self, rating: list[int]) -> int:
        N = len(rating)
        res = 0

        for i in range(N):
            for j in range(i+1, N):
                if rating[i] < rating[j] or rating[i] > rating[j]:
                    for k in range(j+1, N):
                        if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                            res += 1
        return res
    

    def numTeams(self, rating: list[int]) -> int:
        N = len(rating)
        res = 0

        @cache
        def countIncreasing(cur_idx, cur_num):
            if cur_idx == N:
                return 0
            if cur_num == 3:
                return 1
            
            teams = 0
            for next_idx in range(cur_idx+1, N):
                if rating[next_idx] > rating[cur_idx]:
                    teams += countIncreasing(next_idx, cur_num + 1)
            return teams
        
        @cache
        def countDecreasing(cur_idx, cur_num):
            if cur_idx == N:
                return 0
            if cur_num == 3:
                return 1
            
            teams = 0
            for next_idx in range(cur_idx+1, N):
                if rating[next_idx] < rating[cur_idx]:
                    teams += countDecreasing(next_idx, cur_num + 1)
            return teams

        for i in range(N):
            res += countIncreasing(i, 1) + countDecreasing(i, 1)
        return res
    

    def numTeams(self, rating: list[int]) -> int:
        N = len(rating)
        res = 0
        increasing_dp = [[0] * 4 for _ in range(N)]
        decreasing_dp = [[0] * 4 for _ in range(N)]

        for i in range(N):
            increasing_dp[i][1] = decreasing_dp[i][1] = 1
        
        for count in [2,3]:
            for i in range(N):
                for j in range(i+1, N):
                    if rating[i] > rating[j]:
                        decreasing_dp[j][count] += decreasing_dp[i][count-1]
                    if rating[i] < rating[j]:
                        increasing_dp[j][count] += increasing_dp[i][count-1]
        
        
        for i in range(N):
            res += (increasing_dp[i][3] + decreasing_dp[i][3])

        return res

    def numTeams(self, rating: list[int]) -> int:
        N = len(rating)
        res = 0

        for i in range(N):
            mid = rating[i]
            left = 0
            right = 0

            for j in range(i):
                if rating[j] < mid:
                    left += 1
            for j in range(i+1, N):
                if mid < rating[j]:
                    right += 1

            res += left * right
            
            left = i - left
            right = N - i - 1 - right

            # for j in range(i):
            #     if rating[j] > mid:
            #         left += 1
            
            # for j in range(i+1, N):
            #     if rating[j] < mid:
            #         right += 1
            
            res += left * right
        
        return res




                
print(Solution().numTeams([1,2,3,4]))
print(Solution().numTeams([2,5,3,4,1]))
print(Solution().numTeams([3,7,5,6]))