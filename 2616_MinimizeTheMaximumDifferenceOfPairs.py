class Solution:
    def minimizeMax(self, nums, p) -> int:

        if p == 0:
            return 0

        N = len(nums)
        pairs = []

        for i in range(N):
            check = 999999999
            candidate = i
            for j in range(i+1, N):
                if abs(nums[i] - nums[j]) <= check:
                    candidate = j
                    check = abs(nums[i] - nums[j])
            
            if candidate == i:
                continue
            pairs.append(abs(nums[i] - nums[candidate]))

        pairs.sort()

        return max(pairs[0:p])
    

# print(Solution().minimizeMax([10,1,2,7,1,3], 2))
# print(Solution().minimizeMax([4,2,1,2], 1))
print(Solution().minimizeMax([3,4,1,2,1], 2))


            
                


        