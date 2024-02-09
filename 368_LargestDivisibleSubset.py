from functools import cache

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        self.ans = []

        def dp(curIdx, temp):
            if len(temp) > len(self.ans):
                self.ans = list(temp)
            
            for i in range(curIdx, N):
                if nums[i] % temp[-1] == 0:
                    temp.append(nums[i])
                    dp(i+1, temp)
                    temp.pop()


        for i in range(0, N):
            dp(i+1, [nums[i]])
        return self.ans
    

    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        all_set = []
        nums.sort()
        ans = []
        
        for i in range(N):
            all_set.append([nums[i]])
        
        for i in range(N):
            for cur_list in all_set:
                if nums[i] != cur_list[-1] and ((nums[i] % cur_list[-1]) == 0):
                    new_list = list(cur_list)
                    new_list.append(nums[i])
                    all_set.append(new_list)
        
        for cur_list in all_set:
            if len(cur_list) > len(ans):
                ans = cur_list
        return ans
    

    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        ans = set()
        subsets = {nums[0]: set([nums[0]])}

        for i in range(1, N):
            temp = set()
            for k, subset in subsets.items():
                if nums[i] % k == 0:
                    if len(subset) > len(temp):
                        temp = subset
            subsets[nums[i]] = temp | {nums[i]}

        for k, subset in subsets.items():
            if len(subset) > len(ans):
                ans = subset
        return sorted(list(ans))
    
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()

        all_set = {-1: set()}

        for i in range(N):
            cur_num = nums[i]
            temp = []
            for k in all_set:
                if cur_num % k == 0:
                    temp.append(all_set[k])
            all_set[nums[i]] = max(temp, key=len) | {cur_num}

            # all_set[cur_num] = max([all_set[k] for k in all_set if cur_num % k == 0], key=len) | {cur_num}

        return list(max(all_set.values(), key=len))
    
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:

        nums.sort()

        all_set = {-1: set()}

        for n in nums:
            all_set[n] = max([all_set[map_key] for map_key in all_set if n % map_key == 0], key=len) | {n}

        return max(all_set.values(), key=len)
    
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        
        dp = [1] * N
        max_idx = 0

        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > dp[max_idx]:
                max_idx = i
        
        ans = [nums[max_idx]]
        for cur_idx in range(max_idx-1, -1, -1):
            if dp[cur_idx]+1 == dp[max_idx] and nums[max_idx] % nums[cur_idx] == 0:
                ans.append(nums[cur_idx])
                max_idx = cur_idx
        
        return reversed(ans)
    
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        
        @cache
        def dp(cur):

            res = []
            for i in range(0,cur):
                if nums[cur] % nums[i] == 0:
                    temp = dp(i)
                    res = max([res, temp], key=len)
            
            res = res.copy()
            res.append(nums[cur])

            return res
        
        ans = []
        for i in range(N):
            ans = max([ans, dp(i)], key=len)
        return ans

    
print(Solution().largestDivisibleSubset([4,8,10,240]))
print(Solution().largestDivisibleSubset([2,3,4,9,8]))
print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
# print(Solution().largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))