import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = ((1+n) * n) >> 1
        left_sum = 1
        res = 1

        while left_sum <= right_sum:
            if left_sum == right_sum:
                return res
            right_sum -= res
            res += 1
            left_sum += res
        return -1
    
    def pivotInteger(self, n: int) -> int:
        
        for x in range(1, n+1):
            left_sum = 0
            right_sum = 0
            for i in range(1, n+1):
                if i <= x:
                    left_sum += i
                if i >= x:
                    right_sum += i
            if left_sum == right_sum:
                return x
        return -1
    
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        left = 1
        right = n
        left_val = left
        right_val = right

        while left < right:
            if left_val == right_val and left + 1 == right -1:
                return left + 1
            if left_val > right_val:
                right -= 1
                right_val += right
            else:
                left += 1
                left_val += left
            
        return -1
    
    def pivotInteger(self, n: int) -> int:

        left = 0
        right = n

        while left <= right:
            pivot = left + ((right - left) >> 1)
            left_sum = ((1 + pivot-1) * (pivot-1)) >> 1
            right_sum = ((pivot + 1 + n) * (n-pivot)) >> 1

            if left_sum == right_sum:
                return pivot
            else:
                if left_sum < right_sum:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1
    
    '''
    (1+P) * P == (P+N) * ((N+1) - P)
    P + P^2 == P(N+1) + N(N+1) - P^2 - PN
    P + P^2 == PN + P + N^2 + N - P^2 -PN
    P + P^2 == P + N^2 + N - P^2
    P^2 == N^2 + N - P^2
    2 * P^2 == N(N+1)
    P^2 == N(N+1) / 2(total sum)
    '''
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = n
        total = ((1 + n) * n) >> 1

        while left <= right:
            pivot = left + ((right - left) >> 1)
            
            if pivot * pivot == total:
                return pivot
            else:
                if pivot * pivot < total:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1
    
    '''
    P^2 == N(N+1) / 2(total sum)
    P = sqrt( (N(N+1) / 2) )
    '''
    def pivotInteger(self, n: int) -> int:
        total = (n * n + n) >> 1
        res = int(math.sqrt(total))
        return res if res * res == total else -1
 

    
print(Solution().pivotInteger(8))
print(Solution().pivotInteger(1))
print(Solution().pivotInteger(4))