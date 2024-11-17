class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0

        def check(cur_idx, dir, copy_list):

            while 0 <= cur_idx < N:
                if copy_list[cur_idx] != 0:
                    copy_list[cur_idx] -= 1
                    dir = -1 if dir == 1 else 1
                    
                cur_idx += dir
            
            for n in copy_list:
                if n != 0:
                    return False
            return True
        
        for i, n in enumerate(nums):
            if n == 0:
                ans += 1 if check(i, 1, list(nums)) else 0
                ans += 1 if check(i, -1, list(nums)) else 0
        
        return ans
    

    def countValidSelections(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        
        for i in range(N):
            if nums[i] == 0:
                left_sum = 0
                right_sum = 0

                for j in range(0, i):
                    left_sum += nums[j]

                for j in range(i+1, N):
                    right_sum += nums[j]
                
                if left_sum == right_sum:
                    ans += 2
                elif left_sum + 1 == right_sum or left_sum == right_sum + 1:
                    ans += 1
        return ans
    

    def countValidSelections(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(N):
            cur_num = nums[i]
            if nums[i] == 0:
                if left_sum == right_sum:
                    ans += 2
                elif abs(left_sum - right_sum) == 1:
                    ans += 1
            else:
                left_sum += cur_num
                right_sum -= cur_num
        return ans


    
print(Solution().countValidSelections([1,0,2,0,3]))
print(Solution().countValidSelections([2,3,4,0,4,1,0]))
print(Solution().countValidSelections([16,13,10,0,0,0,10,6,7,8,7]))
