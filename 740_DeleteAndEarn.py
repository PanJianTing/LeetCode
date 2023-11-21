from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums) -> int:
        all_nums = sorted(list(set(nums)))
        N = len(all_nums)
        cnt_map = defaultdict(int)
        dp = [0] * N

        for n in nums:
            cnt_map[n] += 1

        dp[0] = cnt_map[all_nums[0]] * all_nums[0]

        for i in range(1, N):
            cur = all_nums[i]
            cnt = cnt_map[cur]
            cur_earn = cur * cnt
            if cur - all_nums[i-1] > 1:
                dp[i] = cur_earn + dp[i-1]
            else:
                dp[i] = max(cur_earn, dp[i-1])
                if i - 2 >= 0:
                    dp[i] = max(dp[i-1], dp[i-2] + cur_earn)
        return max(dp)
    
    def deleteAndEarn(self, nums) -> int:
        all_nums = sorted(list(set(nums)))
        N = len(all_nums)
        cnt_map = defaultdict(int)
        earn1, earn2 = 0, 0

        for n in nums:
            cnt_map[n] += 1


        for i in range(N):
            n = all_nums[i]
            cur_earn = cnt_map[n] * n
            if n - all_nums[i-1] == 1:
                earn1, earn2 = earn2, max(earn2, earn1 + cur_earn)
            else:
                earn1, earn2 = earn2, cur_earn + earn2

        return max(earn1, earn2)


print(Solution().deleteAndEarn([3,4,2]))
print(Solution().deleteAndEarn([2,2,3,3,3,4]))
print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]))
print(Solution().deleteAndEarn([3,1]))