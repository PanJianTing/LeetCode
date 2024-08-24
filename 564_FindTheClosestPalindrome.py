class Solution:
    def nearestPalindromic(self, n: str) -> str:
        N = len(n)
        origin_num = int(n)
        cur_diff = float('inf')
        res = float('inf')
        idx = (N >> 1) - 1
        if N & 1:
            idx = N >> 1

        first_half = int(n[:idx+1])
        
        def get_palindrome(num):
            res = num
            if N & 1:
                num //= 10

            while num > 0:
                res = res * 10 + num % 10
                num //= 10
            
            return res
        
        all_possible = []
        
        all_possible.append(get_palindrome(first_half))
        all_possible.append(get_palindrome(first_half+1))
        all_possible.append(get_palindrome(first_half-1))
        all_possible.append((10 ** (N-1)) - 1)
        all_possible.append((10 ** N) + 1)

        for cur in all_possible:
            if cur == origin_num:
                continue
            diff = abs(cur - origin_num)
            if diff < cur_diff:
                res = cur
                cur_diff = diff
            elif diff == cur_diff:
                res = min(res, cur)

        return str(res)
        


            
    
print(Solution().nearestPalindromic("11"))
print(Solution().nearestPalindromic("1"))
print(Solution().nearestPalindromic("123"))
print(Solution().nearestPalindromic("1234"))
print(Solution().nearestPalindromic("100"))