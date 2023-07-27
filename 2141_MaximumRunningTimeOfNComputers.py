class Solution:

    # Sol #1 Sort and Prefix sum
    def maxRunTime(self, N, batteries) -> int:

        batteries = sorted(batteries)

        lives = batteries[len(batteries) - N:]

        extra = 0

        for i in range(0, len(batteries)-N):
            extra += batteries[i]

        res = lives[0]
        for i in range(0, N-1):
            need = lives[i+1] - lives[i]

            if extra > (need * (i+1)):
                extra -= (need * (i+1))
                res = lives[i+1]
            else:
                res = lives[i] + (extra // (i+1))
                extra = 0
                break
        if extra > 0:
            res += (extra // N)
        return res
    
    def maxRunTime(self, N, batteries) -> int:

        batteries.sort()

        lives = batteries[-N:]

        extra = sum(batteries[:-N])

        for i in range(0, N-1):
            need = lives[i+1] - lives[i]

            if extra > (need * (i+1)):
                extra -= (need * (i+1))
            else:
                return lives[i] + (extra // (i+1))
                
        return lives[-1] + (extra // (N))
    
    def maxRunTime(self, N, batteries) -> int:

        sumPower = sum(batteries)
        left = 1
        right = sumPower // N

        while left <= right:
            mid = left + ((right - left) >> 1)

            extra = 0
            for p in batteries:
                extra += min(p, mid)
            
            if extra >= (mid * N):
                left = mid + 1 
            else:
                right = mid - 1

        return right
    
    def maxRunTime(self, N, b) -> int:
        b.sort()
        su = sum(b)

        while b[-1] > (su // N):
            N -= 1
            su -= b.pop()

        return su // N

print(Solution().maxRunTime(2, [3, 3, 3]))          # 4
print(Solution().maxRunTime(2, [1, 1, 1, 1]))       # 2
print(Solution().maxRunTime(3, [10, 10, 3, 5]))     # 8
print(Solution().maxRunTime(1, [53, 96]))           # 149
print(Solution().maxRunTime(2, [4, 3, 3]))          # 5
print(Solution().maxRunTime(2, [7, 3, 3]))          # 6



        