class Solution:
    def judgeSquareSum(self, c: int) -> int:
        all_square = set()
        cur_num = 0
        while cur_num ** 2 <= c:
            all_square.add(cur_num ** 2)
            cur_num += 1
        
        for n in all_square:
            if (c - n) in all_square:
                return True
        return False
    

    def judgeSquareSum(self, c: int) -> int:
        a = 0
        
        while a ** 2 <= c:
            b = 0
            while b ** 2 <= c:
                if (a ** 2) + (b ** 2) == c:
                    return True
                b += 1
            a += 1

        return False
    
    def judgeSquareSum(self, c: int) -> int:
        a = 0

        while a ** 2 <= c:
            b = c - a ** 2
            sum = 0
            cur = 1
            while sum < b:
                sum += cur
                cur += 2
            if sum == b:
                return True
            a += 1
        return False
    
    def judgeSquareSum(self, c: int) -> int:
        all_square = []
        cur_num = 0
        while cur_num ** 2 <= c:
            all_square.append(cur_num ** 2)
            cur_num += 1

        l = 0
        r = len(all_square) - 1

        while l <= r:
            if all_square[l] + all_square[r] > c:
                r -= 1
            elif all_square[l] + all_square[r] < c:
                l += 1
            else:
                return True
        return False
    
    def judgeSquareSum(self, c: int) -> int:
        a = 0

        while a * a <= c:
            b = c - a ** 2
            
            l = 0
            r = b

            while l <= r:
                m = l + ((r - l) >> 1)
                if m ** 2 > b:
                    r = m - 1
                elif m ** 2 < b:
                    l = m + 1
                else:
                    return True
            a += 1
        return False
    

    def judgeSquareSum(self, c: int) -> int:
        a = 2

        while a * a < c:
            cnt = 0
            if c % a == 0:
                while (c % a) == 0:
                    cnt += 1
                    c /= a
                if (a % 4 == 3) and (cnt % 2):
                    return False
            a += 1
        return c % 4 != 3
    
    
# print(Solution().judgeSquareSum(5)) # T
# print(Solution().judgeSquareSum(3)) # F
# print(Solution().judgeSquareSum(4)) # T
# print(Solution().judgeSquareSum(2)) # T
print(Solution().judgeSquareSum(25))