from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        N = len(nums)

        def generateSubset(idx, mask):
            if N == idx:
                if mask > 0:
                    return 1
                return 0
            
            isValid = True
            for i in range(idx):
                if ((1 << i) & mask) and abs(nums[idx] - nums[i]) == k:
                    isValid = False
                    break
            skip = generateSubset(idx+1, mask)
            take = 0
            if isValid:
                take = generateSubset(idx+1, mask + (1 << idx))
            return skip + take
            
        return generateSubset(0, 0)
    
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        # cnt_map = defaultdict(int)

        def dp(idx, cnt_map):
            if idx == N:
                return 1
            
            total_cnt = dp(idx+1, cnt_map)

            if (nums[idx] - k) not in cnt_map:
                cnt_map[nums[idx]] += 1
                total_cnt += dp(idx + 1, cnt_map)
                cnt_map[nums[idx]] -= 1
                if cnt_map[nums[idx]] == 0:
                    del cnt_map[nums[idx]]
            
            return total_cnt

        return dp(0, defaultdict(int)) - 1

        
    
print(Solution().beautifulSubsets([2,4,6], 2))
print(Solution().beautifulSubsets([4,2,5,9,10,3], 1))
print(Solution().beautifulSubsets([942,231,247,267,741,320,844,276,578,659,96,697,801,892,752,948,176,92,469,595], 473))