import heapq

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        hq = []

        for interval in range(1, N):
            for i in range(N-interval):
               hq.append(nums[i + interval] - nums[i])

        hq.sort()
        return hq[k-1]
    
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        bucket = [0] * (nums[-1] - nums[0] + 1)
        cur_cnt = 0

        for i in range(N):
            for j in range(i+1, N):
                bucket[nums[j] - nums[i]] += 1
        
        for i in range(len(bucket)):
            cur_cnt += bucket[i]
            if cur_cnt >= k:
                return i
            
        return -1


print(Solution().smallestDistancePair([1,3,1], 1))
print(Solution().smallestDistancePair([1,1,1], 2))
print(Solution().smallestDistancePair([1,6,1], 3))
print(Solution().smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18))
        