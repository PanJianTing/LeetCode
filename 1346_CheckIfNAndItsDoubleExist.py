class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()

        for n in arr:
            if ((n << 1) in seen) or ((n & 1 == 0) and ((n >> 1) in seen)):
                return True

            seen.add(n)
        return False
    

print(Solution().checkIfExist([-2,0,10,-19,4,6,-8]))
        