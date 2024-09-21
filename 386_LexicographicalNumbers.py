class Solution:
    def lexicalOrder(self, N: int) -> list[int]:
        res = []

        def dp(cur):
            if cur > N:
                return
            
            if cur != 0:
                res.append(cur)
            for i in range(10):
                if cur * 10 + i == cur:
                    continue
                dp(cur * 10 + i)
            
            return
        
        dp(0)
    
        return res
    
    def lexicalOrder(self, N: int) -> list[int]:
        res = []

        def dp(cur):
            if cur > N:
                return
            
            res.append(cur)
            for i in range(10):
                dp(cur*10 + i)
            
            return
        for i in range(1, 10):
            dp(i)
        
        return res
    

    def lexicalOrder(self, N: int) -> list[int]:
        res = []

        cur = 1

        for i in range(N):
            res.append(cur)

            if cur * 10 <= N:
                cur *= 10
            else:
                while cur % 10 == 9 or cur >= N:
                    cur //= 10
                cur += 1
        
        return res

    
print(Solution().lexicalOrder(130))
print(Solution().lexicalOrder(2))
