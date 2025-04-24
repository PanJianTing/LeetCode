from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        N = len(nums)
        all_num = set()
        num_set = set()
        cnt_map = defaultdict(int)
        res = 0
        l = 0

        for i in range(N):
            all_num.add(nums[i])

        for r in range(N):
            num_set.add(nums[r])
            cnt_map[nums[r]] += 1

            while len(num_set) == len(all_num):
                res += N - r
                cnt_map[nums[l]] -= 1
                if cnt_map[nums[l]] == 0:
                    num_set.remove(nums[l])
                l += 1
        
        return res

            
# print(Solution().countCompleteSubarrays([1,3,1,2,2]))
print(Solution().countCompleteSubarrays([5,5,5,5,1]))




        