from math import sqrt

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        lim = int(sqrt(r)) + 1
        is_prime = [True] * lim
        is_prime[0] = is_prime[1] = True

        for i in range(2, lim):
            if is_prime[i]:
                for j in range(i*i, lim, i):
                    is_prime[j] = False

        special_count = 0
        
        for i in range(2, lim):
            if is_prime[i]:
                if l <= i * i <= r:
                    special_count += 1
        
        total_cnt = r - l + 1

        return total_cnt - special_count
    
# print(Solution().nonSpecialCount(5, 7))
print(Solution().nonSpecialCount(4, 16))
print(Solution().nonSpecialCount(5, 25))
print(Solution().nonSpecialCount(1, 2))
print(Solution().nonSpecialCount(182, 18677))