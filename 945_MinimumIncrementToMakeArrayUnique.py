class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        seen = set()
        dups = []
        res = 0
        leak = []

        min_num = min(nums)
        max_num = max(nums)

        for n in nums:
            if n in seen:
                dups.append(n)
            else:
                seen.add(n)

        for i in range(min_num+1, max_num):
            if i not in seen:
                leak.append(i)
        
        idx = 0
        max_num += 1
        
        dups.sort()
        for n in dups:
            handle = False
            while idx < len(leak):
                if leak[idx] > n:
                    res += leak[idx] - n
                    idx += 1
                    handle = True
                    break
                idx += 1
            if handle == False:
                res += max_num - n
                max_num += 1
            
        return res
    
    def minIncrementForUnique(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        nums.sort()

        for i in range(1, N):
            if nums[i] <= nums[i-1]:
                res += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1

        return res
    
    def minIncrementForUnique(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        max_num = max(nums)

        cnt_list = [0] * (N + max_num+1)

        for n in nums:
            cnt_list[n] += 1
        
        for i in range(N + max_num):
            if cnt_list[i] < 2:
                continue

            cur_cnt = cnt_list[i]
            res += cur_cnt - 1
            cnt_list[i+1] += (cur_cnt - 1)
        return res
            

print(Solution().minIncrementForUnique([0,0]))
print(Solution().minIncrementForUnique([1,2,2]))
print(Solution().minIncrementForUnique([3,2,1,2,1,7]))
print(Solution().minIncrementForUnique([0,2,2]))
print(Solution().minIncrementForUnique([4,4,7,5,1,9,4,7,3,8]))