from collections import defaultdict
import heapq


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        def check(target, num):
            target_list = []
            num_list = []

            while target > 0 or num > 0:
                target_list.append(target % 10)
                num_list.append(num % 10)
                target //= 10
                num //= 10
            

            for i in range(len(num_list)):
                for j in range(i+1, len(num_list)):
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    if num_list == target_list:
                        return True
                    num_list[j], num_list[i] = num_list[i], num_list[j]

            return False

        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                        res += 1
                else:
                    if check(nums[i], nums[j]):
                        res += 1
        
        return res

print(Solution().countPairs([3,12,30,17,21]))
print(Solution().countPairs([1,1,1,1,1]))
print(Solution().countPairs([123,231]))
print(Solution().countPairs([8,12,5,5,14,3,12,3,3,6,8,20,14,3,8]))
