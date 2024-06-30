from itertools import groupby

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = [0] * 2
        end = [0] * 2

        for n in nums:
            count[n & 1] += 1
            end[n & 1] = max(end[n & 1], end[1-n & 1] + 1)


        return max(max(count), max(end))
    

print(Solution().maximumLength([1,2,3,4]))
print(Solution().maximumLength([1,2,1,1,2,1,2]))
print(Solution().maximumLength([1,3]))