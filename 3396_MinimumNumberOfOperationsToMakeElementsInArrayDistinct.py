from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        N = len(nums)
        l = 0
        cnt_map = defaultdict(int)
        ans = 0

        for n in nums:
            cnt_map[n] += 1
        
        def check():
            for k, v in cnt_map.items():
                if v > 1:
                    return True
            return False
        
        while check():
            ans += 1
            for _ in range(3):
                if l < N:
                    cnt_map[nums[l]] -= 1
                    l += 1

        return ans
    
    def minimumOperations(self, nums: list[int]) -> int:
        N = len(nums)
        seen = set()

        for i in range(N-1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0

    
print(Solution().minimumOperations([1,2,3,4,2,3,3,5,7]))
        