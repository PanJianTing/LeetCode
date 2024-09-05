class Solution:
    def missingRolls(self, rolls: list[int], mean: int, N: int) -> list[int]:
        M = len(rolls)
        total = mean * (M + N)
        remaings = total - sum(rolls)
        
        if not (N <= remaings <= 6 * N):
            return []
        
        res = []
        cur_n = N

        while cur_n > 0:
            num = remaings // cur_n
            res.append(num)
            remaings -= num
            cur_n -= 1

        return res
    
    def missingRolls(self, rolls: list[int], mean: int, N: int) -> list[int]:
        M = len(rolls)
        total = mean * (M + N)
        remaings = total - sum(rolls)
        
        if not (N <= remaings <= 6 * N):
            return []
        
        res = [remaings // N] * N
        remaings = remaings % N

        for i in range(remaings):
            res[i] += 1

        return res

print(Solution().missingRolls([3,2,4,3], 4, 2))
print(Solution().missingRolls([1,5,6], 3, 4))
print(Solution().missingRolls([1,2,3,4], 6, 4))
print(Solution().missingRolls([6,3,4,3,5,3], 1, 6))
print(Solution().missingRolls([4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53))

