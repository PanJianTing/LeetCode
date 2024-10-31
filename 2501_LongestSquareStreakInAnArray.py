from collections import defaultdict
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        N = len(nums)
        all_num = set(nums)

        # nums.sort()
        process_num = set()
        ans = 0

        for i in range(N):
            cur_n = nums[i]
            if cur_n in process_num:
                continue

            cur_long = 1

            while cur_n * cur_n in all_num:
                cur_long += 1
                cur_n = cur_n * cur_n
                process_num.add(cur_n * cur_n)
            
            process_num.add(cur_n)
            ans = max(ans, cur_long)

        return -1 if ans < 2 else ans
    

    def longestSquareStreak(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()
        process_num = set()
        ans = 0

        def bs(target):
            l = 0
            r = N-1

            while l <= r:
                m = l + ((r - l) >> 1)

                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return -1

        for i in range(N):
            cur_n = nums[i]
            if cur_n in process_num:
                continue

            cur_long = 1

            while bs(cur_n * cur_n) != -1:
                cur_long += 1
                cur_n = cur_n * cur_n
                process_num.add(cur_n * cur_n)
            
            process_num.add(cur_n)
            ans = max(ans, cur_long)

        return -1 if ans < 2 else ans
    

    def longestSquareStreak(self, nums: list[int]) -> int:
        streak_map = defaultdict(int)
        nums.sort()
        ans = 0

        for n in nums:
            root = int(sqrt(n))

            if root * root == n and root in streak_map:
                streak_map[n] = streak_map[root] + 1
                ans = max(streak_map[n], ans)
            else:
                streak_map[n] = 1
        return -1 if ans < 2 else ans


    
# print(Solution().longestSquareStreak([4,3,6,16,8,2]))
print(Solution().longestSquareStreak([2,4,4,2]))



