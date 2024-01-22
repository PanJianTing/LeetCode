from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        allSum = sum(nums)
        setSum = sum(set(nums))
        allRangeSum = sum(range(1, len(nums) + 1))

        return [allSum - setSum, allRangeSum - setSum]


    def findErrorNums(self, nums: list[int]) -> list[int]:
        count = len(nums)
        allSum = ((1+count) * count)//2

        nowDic = {}
        repeatCount = 0

        for n in nums:
            if n not in nowDic:
                allSum -= n
                nowDic[n] = 1
            else:
                repeatCount = n


        return [repeatCount, allSum]
    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dup = -1
        miss = -1
        N = len(nums)
        for i in range(1, N+1):
            cnt = 0
            for num in nums:
                if i == num:
                    cnt += 1
            
            if cnt == 2:
                dup = i
            elif cnt == 0:
                miss = i
        return [dup, miss]
    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dup = -1
        miss = -1
        N = len(nums)
        for i in range(1, N+1):
            cnt = 0
            for num in nums:
                if i == num:
                    cnt += 1
            
            if cnt == 2:
                dup = i
            elif cnt == 0:
                miss = i

            if dup > 0 and miss > 0:
                break
        return [dup, miss]
    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        N = len(nums)
        dup = -1
        miss = 1
        for i in range(1, N):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1] + 1:
                miss = nums[i-1] + 1
            
        return [dup, miss if nums[N-1] == N else N]
    

    def findErrorNums(self, nums: list[int]) -> list[int]:
        N = len(nums)
        cnt_map = defaultdict(int)
        res = [0,0]
        for n in nums:
            cnt_map[n] += 1
        
        for i in range(1, N+1):
            if cnt_map[i] == 2:
                res[0] = i
            elif cnt_map[i] == 0:
                res[1] = i
        
        return res

    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        N = len(nums)
        cnt_list = [0] * (N+1)
        miss = -1
        dup = -1

        for n in nums:
            cnt_list[n] += 1
        
        for i in range(1, N+1):
            if cnt_list[i] == 2:
                dup = i
            elif cnt_list[i] == 0:
                miss = i
        return [dup, miss]
    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dup = -1
        miss = 1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
            
        for i in range(1, len(nums)):
            if nums[i] > 0:
                miss = i+1
        return [dup, miss]



# print(Solution().findErrorNums([1,2,2,4]))
# print(Solution().findErrorNums([1,2,3,3]))
print(Solution().findErrorNums([3,2,3,4,6,5]))