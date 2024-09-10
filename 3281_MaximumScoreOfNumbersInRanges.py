class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        N = len(start)
        start.sort()
        l = 0
        r = start[-1] - start[0] + d
        res = 0

        def isPossible(score) -> bool:
            pre = start[0]
            for i in range(1, N):
                if start[i] <= pre + score <= start[i] + d:
                    pre += score
                elif pre + score < start[i]:
                    pre = start[i]
                else:
                    return False
                # if start[i] + d - pre < score:
                #     return False
                # pre = max(start[i], pre + score)

            return True
        
        while l <= r:
            m = l + ((r - l) >> 1)

            if isPossible(m):
                res = m
                l = m+1
            else:
                r = m-1
        return res
    
# print(Solution().maxPossibleScore([6,0,3], 2))
print(Solution().maxPossibleScore([2,6,13,13], 5))