class Solution:
    def longestSubarray(self, nums) -> int:
        cntCount = []
        cnt = 0
        for n in nums:
            if n == 0:
                cntCount.append(cnt)
                cnt = 0
            else:
                cnt += 1
        if cnt:
            cntCount.append(cnt)
        
        if len(cntCount) == 1:
            return cntCount[0] - 1
        
        ans = 0
        for i in range(0, len(cntCount) - 1):
            ans = max(ans, cntCount[i] + cntCount[i+1])

        return ans
    
    def longestSubarray(self, nums) -> int:
        N = len(nums)
        zero = 0
        longest = 0
        start = 0

        for i in range(N):
            zero += 1 if nums[i] == 0 else 0

            while zero > 1:
                zero -= 1 if nums[start] == 0 else 0
                start += 1
            longest = max(longest, i-start)
        
        return longest
    

    def longestSubarray(self, nums) -> int:
        k = 1
        i = 0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i
    
    def longestSubarray(self, A):
        prev = None
        curr = 0
        ans = 0

        for n in A:
            if n:
                curr += 1
            else:
                if prev == None:
                    prev = 0
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0

        if prev == None:
            return curr - 1
        return max(ans, curr + prev)
    
print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))
print(Solution().longestSubarray([0,0,0]))


