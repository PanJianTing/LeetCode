class Solution:
    
    def myPow(self, x, n) -> float:

        if n == 0:
            return 1
        
        minus = n < 0

        ans = x
        
        for _ in range(1, abs(n)):
            ans *= x
        
        return 1/ans if minus else ans
    
    def cal(self, x, n) -> float:
        if n == 0: return 1
        if n < 0: return 1.0 / self.cal(x, -n)

        if n % 2:
            return x * self.cal(x*x, (n - 1) // 2)
        
        return self.cal(x*x, n // 2)
    
    def myPow(self, x, n) -> float:
        return self.cal(x, n)
    

    def myPow(self, x, n) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1

        while n != 0:

            if n % 2:
                res *= x
                n -= 1
            
            x = x * x
            n = n // 2
        
        return res
                

    

print(Solution().myPow(2.0, 10))
print(Solution().myPow(2.1, 3))
print(Solution().myPow(2.0, -2))