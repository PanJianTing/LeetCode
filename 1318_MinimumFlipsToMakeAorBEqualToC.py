from itertools import zip_longest

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        flipCnt = 0

        def toBit(cnt):
            mask = 1
            res = []

            while cnt:
                res.append(cnt & mask)
                cnt = cnt >> 1
            # res.reverse()

            return res
        
        A = toBit(a)
        B = toBit(b)
        C = toBit(c)

        for a_bit, b_bit, c_bit in zip_longest(A,B,C, fillvalue=0):

            # print(a_bit, b_bit, c_bit)

            if (a_bit | b_bit) == c_bit:
                continue
            else:
                if c_bit:
                    if not (a_bit or b_bit):
                        flipCnt += 1
                else:
                    if a_bit and b_bit:
                        flipCnt += 2
                    else:
                        flipCnt += 1

        return flipCnt
    

    def minFlips(self, a, b, c) -> int:

        res = 0

        while a or b or c:
            a_b = a & 1
            b_b = b & 1
            c_b = c & 1

            if c_b:
                if (a_b == 0) & (b_b == 0):
                    res += 1
            else:
                res += a_b + b_b
            a >>= 1
            b >>= 1
            c >>= 1
        return res
    
    def minFlips(self, a, b, c) -> int:
        return bin((a | b) ^ c).count("1") + bin((a & b) & ((a | b) ^ c)).count("1")
    
print(Solution().minFlips(2,6,5))
print(Solution().minFlips(4,2,7))
print(Solution().minFlips(1,2,3))