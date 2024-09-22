class Solution:
    def findKthNumber(self, N: int, k: int) -> int:
        res = []

        def dp(cur):
            if cur > N:
                return
            res.append(cur)

            for i in range(10):
                dp(cur * 10 + i)

            return

        for i in range(1, 10):
            dp(i)
        
        return res[k-1]

    def findKthNumber(self, N: int, k: int) -> int:
        cur_num = 1

        for i in range(k-1):

            if cur_num * 10 <= N:
                cur_num *= 10
            else:
                while cur_num % 10 == 9 or cur_num >= N:
                    cur_num //= 10
                cur_num += 1
        return cur_num
    
    def findKthNumber(self, N: int, k: int) -> int:
        cur = 1
        k -= 1

        def step(pre1, pre2):
            res = 0
            while pre1 <= N:
                res += min(N+1, pre2) - pre1
                pre1 *= 10
                pre2 *= 10
            return res
        
        while k > 0:
            cur_step = step(cur, cur+1)

            if cur_step <= k:
                cur += 1
                k -= cur_step
            else:
                cur *= 10
                k -= 1
        
        return cur
    

print(Solution().findKthNumber(13, 2))
print(Solution().findKthNumber(1, 1))
        
