from collections import defaultdict

class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        while nums[0] > 0:
            all_digit = defaultdict(int)
            for i in range(N):
                all_digit[(nums[i] % 10)] += 1
                nums[i] //= 10

            for i in range(10):
                res += all_digit[i] * (N - all_digit[i])

        return res // 2
            

print(Solution().sumDigitDifferences([13,23,12])) # 4
print(Solution().sumDigitDifferences([10,10,10,10])) # 0
print(Solution().sumDigitDifferences([50,28,48])) # 5
print(Solution().sumDigitDifferences([824,843,837,620,836,234,276,859])) # 5
            
            
