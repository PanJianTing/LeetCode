class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        def check(cur):
            all_digit = []

            while cur > 0:
                all_digit.append(cur%10)
                cur //= 10
            n = len(all_digit)
            if n & 1:
                return False
            
            one = all_digit[n>>1:]
            two = all_digit[:n>>1]

            return sum(one) == sum(two) 


        for num in range(low, high+1):
            if check(num):
                ans += 1
        
        return ans
    

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for num in range(low, high+1):

            if 10 < num < 100:
                if num % 11 == 0:
                    ans += 1
            
            if 1000 < num < 10000:
                d1 = num // 1000
                d2 = (num % 1000) // 100
                d3 = (num % 100) // 10
                d4 = num % 10
                l = d1 + d2
                r = d3 + d4
                if l == r:
                     ans += 1
        return ans
    
# print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))
