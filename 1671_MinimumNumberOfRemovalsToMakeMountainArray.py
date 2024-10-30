class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        N = len(nums)

        lis_l = [1] * N
        lds_l = [1] * N

        ans = float('inf')

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_l[i] = max(lis_l[i], lis_l[j] + 1)

        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if nums[i] > nums[j]:
                    lds_l[i] = max(lds_l[i], lds_l[j] + 1)

        for i in range(N):
            if lis_l[i] > 1 and lds_l[i] > 1:
                ans = min(ans, N - (lis_l[i] + lds_l[i] - 1))

        return ans
    

print(Solution().minimumMountainRemovals([1,3,1]))


        
