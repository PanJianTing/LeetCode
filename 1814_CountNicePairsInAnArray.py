from collections import defaultdict

class Solution:

    def rev_num(self, n) -> int:
        count = 0
        digits = []
        revers_num = 0

        while n > 0:
            digits.append(n % 10)
            n //= 10
            count += 1

        for i in range(len(digits)):
            revers_num += digits[i] * (10 ** (count-1))
            count -= 1
        
        return revers_num
    
    #TLE
    def countNicePairs(self, nums) -> int:
        ans = 0
        N = len(nums)
        reverse_nums = []

        for n in nums:
            reverse_nums.append(self.rev_num(n))

        for i in range(N):
            for j in range(i+1, N):
                if nums[i] + reverse_nums[j] == reverse_nums[i] + nums[j]:
                    ans += 1
        return ans
    
    def countNicePairs(self, nums) -> int:
        ans = 0
        cnt_map = defaultdict(int)

        for n in nums:
            # reverse_num = self.rev_num(n)
            reverse_num = int(str(n)[::-1])
            cnt_map[n - reverse_num] += 1
        
        for k in list(cnt_map.keys()):
            count = cnt_map[k]
            ans += ((count * (count - 1)) >> 1)
        
        return ans % (10 ** 9 + 7)
    
    def countNicePairs(self, nums) -> int:

        def rev(n):
            res = 0

            while n > 0:
                res = res * 10 + n % 10
                n //= 10

            return res

        cnt_map = defaultdict(int)
        ans = 0
        
        for n in nums:
            cur = n - rev(n)
            ans += cnt_map[cur]
            cnt_map[cur] += 1
        
        return ans % (10 ** 9 + 7)

    
print(Solution().countNicePairs([42,11,1,97]))
print(Solution().countNicePairs([13,10,35,24,76]))
print(Solution().countNicePairs([432835222,112141211,5408045,456281503,283322436,414281561,37773,286505682]))