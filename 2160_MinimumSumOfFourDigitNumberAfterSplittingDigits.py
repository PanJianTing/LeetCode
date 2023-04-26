class Solution:
    def minimumSum(self, num: int) -> int:
        d = []
        while num > 0:
            d.append(num % 10)
            num //= 10
        d.sort()

        return d[0] * 10 + d[1] * 10 + d[2] + d[3]