class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        cur = 1
        while True:
            if cur not in nums:
                return cur
            cur += 1

    def firstMissingPositive(self, nums: list[int]) -> int:
        N = len(nums)
        seen = [False] * (N+1)

        for n in nums:
            if 1 <= n <= N:
                seen[n] = True
        
        for i in range(1, N+1):
            if seen[i] == False:
                return i
        return N+1
    
    def firstMissingPositive(self, nums: list[int]) -> int:
        N = len(nums)
        contain_one = False

        for i in range(N):
            n = nums[i]
            if n == 1:
                contain_one = True
            if n <= 0 or n > N:
                nums[i] = 1
        if contain_one == False:
            return 1
        
        for n in nums:
            n = abs(n)
            if n == N:
                nums[0] = abs(nums[0]) * -1
            else:
                nums[n] = abs(nums[n]) * -1
        
        for i in range(1, N):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return N
        return N+1
        

    def firstMissingPositive(self, nums: list[int]) -> int:
        N = len(nums)
        cur = 0

        while cur < N:
            pos = abs(nums[cur]) - 1
            if (nums[cur] <= 0 or nums[cur] > N) or nums[cur] == nums[pos]:
                cur += 1
            else:
                nums[cur], nums[pos] = nums[pos], nums[cur]

        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1

print(Solution().firstMissingPositive([1,1]))
print(Solution().firstMissingPositive([1, 1000]))
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([1,2,3]))