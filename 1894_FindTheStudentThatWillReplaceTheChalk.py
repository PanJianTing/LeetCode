class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        N = len(chalk)
        all_sum = sum(chalk)
        k = k % all_sum

        for i in range(N):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        return -1
    
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        N = len(chalk)
        prefix = [0] * N
        prefix[0] = chalk[0]
        
        for i in range(1, N):
            prefix[i] = prefix[i-1] + chalk[i]

        k %= prefix[-1]
        l = 0
        r = N-1

        while l < r:
            m = l + ((r-l) >> 1)

            if prefix[m] <= k:
                l = m+1
            else:
                r = m
        return r


print(Solution().chalkReplacer([5,1,5], 22))
print(Solution().chalkReplacer([3,4,1,2], 25))
