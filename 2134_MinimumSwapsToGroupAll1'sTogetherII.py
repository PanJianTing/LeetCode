class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        N = len(nums)

        def helper(val):
            rightSuffix = [0] * (N+1)

            for i in range(N-1, -1, -1):
                rightSuffix[i] = rightSuffix[i+1]
                if nums[i] == (val ^ 1):
                    rightSuffix[i] += 1
            
            totalNeed = rightSuffix[0]
            curSwapCnt = 0
            miniSwap = totalNeed - rightSuffix[N-totalNeed]

            for i in range(totalNeed):
                if nums[i] == (val ^ 1):
                    curSwapCnt += 1
                remaining = totalNeed - i - 1
                require = ((i+1) - curSwapCnt) + (remaining - rightSuffix[N - remaining])
                miniSwap = min(miniSwap, require)
            
            return miniSwap
        return min(helper(0), helper(1))
    

    def minSwaps(self, nums: list[int]) -> int:
        N = len(nums)

        def helper(val):
            total = 0

            for i in range(N):
                if nums[i] == val:
                    total += 1
            
            if total == 0 or total == N:
                return 0
            
            st = 0
            end = 0
            cur_cnt = 0
            max_cnt = 0

            while end < total:
                if nums[end] == val:
                    cur_cnt += 1
                    max_cnt += 1
                end += 1
            
            while end < N:
                if nums[st] == val:
                    cur_cnt -= 1
                if nums[end] == val:
                    cur_cnt += 1
                
                max_cnt = max(max_cnt, cur_cnt)
                st += 1
                end += 1
            return total - max_cnt
        return min(helper(1), helper(0))
    

    def minSwaps(self, nums: list[int]) -> int:
        total_ones = sum(nums)
        cur_ones = sum(nums[-total_ones:])
        max_ones = cur_ones

        for i in range(len(nums)):
            cur_ones += nums[i]-nums[i-total_ones]
            max_ones = max(max_ones, cur_ones)
        return total_ones - max_ones
    
print(Solution().minSwaps([0,1,0,1,1,0,0]))
print(Solution().minSwaps([0,1,1,1,0,0,1,1,0]))
print(Solution().minSwaps([1,1,0,0,1]))