from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: list[int], MOD: int, k: int) -> int:
        N = len(nums)
        res = 0

        for l in range(N):
            for r in range(l, N):
                cnt = 0
                for i in range(l, r+1):
                    if nums[i] % MOD == k:
                        cnt += 1
                if cnt % MOD == k:
                    res += 1
        
        return res
    

    def countInterestingSubarrays(self, nums: list[int], MOD: int, k: int) -> int:
        N = len(nums)
        prefix_sum = [0] * (N+1)
        res = 0

        for i in range(N):
            n = nums[i]
            prefix_sum[i+1] = prefix_sum[i] + (1 if n % MOD == k else 0)

        for l in range(N+1):
            for r in range(l+1, N+1):
                if (prefix_sum[r] - prefix_sum[l]) % MOD == k:
                    res += 1
        
        return res
    

    def countInterestingSubarrays(self, nums: list[int], MOD: int, k: int) -> int:
        N = len(nums)
        prefix_sum = [0] * (N+1)
        res = 0
        cnt_map = defaultdict(int)

        for i in range(N):
            n = nums[i]
            prefix_sum[i+1] = prefix_sum[i] + (1 if n % MOD == k else 0)

        for r in range(N+1):
            cur_r = prefix_sum[r] % MOD
            res += cnt_map[(cur_r - k) % MOD]
            cnt_map[cur_r] += 1
        
        return res
    
    def countInterestingSubarrays(self, nums: list[int], MOD: int, k: int) -> int:
        N = len(nums)
        cur_r = 0
        res = 0
        cnt_map = defaultdict(int)
        cnt_map[0] = 1

        for r in range(N):
            cur_r += (1 if nums[r] % MOD == k else 0) % MOD
            res += cnt_map[(cur_r - k) % MOD]
            cnt_map[cur_r] += 1
        
        return res

    

print(Solution().countInterestingSubarrays([4,5], 1, 0))
print(Solution().countInterestingSubarrays([3,2,4], 2, 1))
print(Solution().countInterestingSubarrays([3,1,9,6], 3, 0))