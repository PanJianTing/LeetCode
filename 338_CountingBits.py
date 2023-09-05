class Solution:
    def bits(self, n) -> int:

        result = 0

        while n > 0:
            if n % 2 == 1:
                result += 1
            n //= 2

        return result

    def countBits(self, n: int) -> list[int]:

        bitList = []

        for i in range(n+1):

            bitList.append(self.bits(i))
        
        return bitList


class Solution:
    def countBits(self, n):
        ans = []

        for num in range(n+1):
            bits = 0

            while num > 0:
                bits += num % 2
                num >>= 1
            
            ans.append(bits)

        return ans
    
    def countBits(self, n):
        ans = []

        for num in range(n+1):
            bits = 0

            while num != 0:
                num &= num -1
                bits += 1
            
            ans.append(bits)

        return ans
    
    def countBits(self, n):
        ans = [0] * (n+1)
        now = 0
        upper = 1

        while upper < n+1:
            while (now < upper) and (now + upper <= n):
                ans[now+upper] = ans[now] + 1
                now += 1
            now = 0
            upper <<= 1
        
        return ans
    
    def countBits(self, n):
        ans = [0] * (n+1)

        for num in range(1, n+1):
            # ans[num] = ans[num >> 1] + num % 2
            ans[num] = ans[num >> 1] + (num & 1)
        
        return ans
    
    def countBits(self, N):
        ans = [0] * (N+1)

        for num in range(1, N+1):
            ans[num] = ans[num & (num - 1)] + 1
        
        return ans


print(Solution().countBits(2))
print(Solution().countBits(5))



