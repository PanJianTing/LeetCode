class Solution:
    def findKthNumber(self, N: int, k: int) -> int:
        cur = 1
        k -= 1

        def calStep(num1, num2):
            res = 0

            while num1 <= N:
                if num2 <= N:
                    res += num2 - num1
                elif num2 > N:
                    res += N - num1 + 1
                num1 *= 10
                num2 *= 10
            return res
        
        while k > 0:
            step = calStep(cur, cur + 1)

            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1
        
        return cur
        

print(Solution().findKthNumber(13, 2))
print(Solution().findKthNumber(804289384, 42641503))