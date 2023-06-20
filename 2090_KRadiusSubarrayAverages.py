from collections import deque

class Solution:
    def getAverages(self, nums, k) -> list[int]:

        cnt = (k << 1) + 1
        ans = []
        l = -k
        r = k+1
        N = len(nums)
        for n in nums:
            if l >= 0 and r < N+1:
                ans.append(sum(nums[l:r]) // (cnt))
            else:
                ans.append(-1)
            l += 1
            r += 1

        return ans
    
    def getAverages(self, nums, k) -> list[int]:

        cnt = (k << 1) + 1
        q = deque()
        ans = []
        N = len(nums)
        
        for i in range(min(N,k)):
            q.append(nums[i])

        for i in range(k, N):
            q.append(nums[i])
            if len(q) > cnt:
                q.popleft()
            
            if len(q) == cnt:
                ans.append(sum(q) // cnt)
            else:
                ans.append(-1)

        if len(ans) != N:
            for i in range(N-len(ans)):
                ans.append(-1)

        return ans
    

    # my solution window sum
    def getAverages(self, nums, k) -> list[int]:

        cnt = (k << 1) + 1
        ans = []
        l = -k
        r = k+1
        N = len(nums)
        rangeSum = sum(nums[0:r])
        for n in nums:
            if l >= 0 and r < N+1:
                ans.append(rangeSum // (cnt))
            else:
                ans.append(-1)

            if l >= 0:
                rangeSum -= nums[l]
            if r < N:
                rangeSum += nums[r]

            l += 1
            r += 1

        return ans
    
    # Solution #1 prefix sum
    def getAverages(self, nums, k) -> list[int]:

        if k == 0:
            return nums
        N = len(nums)
        ans = [-1] * N
        cnt = (k << 1) + 1

        if cnt > N:
            return ans
        
        prefixSum = [0] * (N+1)

        for i in range(N):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        
        for i in range(k, N-k):
            l = i - k
            r = i + k

            ans[i] = (prefixSum[r+1] - prefixSum[l]) // cnt
        
        return ans
    
    #Solution #2 slide window
    def getAverages(self, nums, k) -> list[int]:

        N = len(nums)
        cnt = (k << 1) + 1
        sumWindow = 0
        ans = [-1] * N

        if k == 0:
            return nums
        
        if cnt > N:
            return ans
        
        for i in range(cnt):
            sumWindow += nums[i]
        
        # another for
        ans[k] = sumWindow // cnt
        for i in range(cnt, N):
            center = i - k
            l =  i - cnt
            sumWindow = sumWindow - nums[l] + nums[i] 
            ans[center] = sumWindow // cnt

        # for i in range(cnt-1, N):
        #     center = i - k
        #     l =  i - cnt + 1
        #     ans[center] = sumWindow // cnt
        #     sumWindow -= nums[l]
        #     if i+1 < N:
        #         sumWindow += nums[i+1]

        return ans
            

    

print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3))
print(Solution().getAverages([100000], 0))
print(Solution().getAverages([8], 100000))