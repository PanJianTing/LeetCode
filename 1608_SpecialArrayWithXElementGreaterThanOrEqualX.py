from bisect import bisect_left

class Solution:
	def specialArray(self, nums: list[int]) -> int:
		ans = 0

		while ans <= len(nums):
			count = 0
			for num in nums:
				if num >= ans:
					count += 1
			if count == ans:
				return ans

			ans += 1

		return -1
	
	def specialArray(self, nums: list[int]) -> int:

		N = len(nums)
		nums.sort()

		for x in range(1, N+1):
			idx = bisect_left(nums, x)
			if x == (N-idx):
				return x

		return -1
	
	def specialArray(self, nums: list[int]) -> int:
		N = len(nums)
		freqs = [0] * (N+1)

		for i in range(N):
			freqs[min(N, nums[i])] += 1

		suffixSum = 0
		for x in range(N, 0, -1):
			suffixSum += freqs[x]
			if x == suffixSum:
				return x
		return -1
	
	

print(Solution().specialArray([3, 5]))
print(Solution().specialArray([0,0]))
print(Solution().specialArray([0,4,3,0,4]))
