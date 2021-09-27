class Solution:

	def maximumDifference(self, nums: list[int]) -> int:
		# 假設nums裡最小的值(mini)是第一個，則跑for往後找，如果其中有遇到較小的值，則把mini換掉，之後再繼續下次的iteration
		# init:因為for loop跑nums[1..n]，因為nums裡只剩nums[0]一個數，故初始狀態時，最小的數為nums[0]
		# maintance: j = 1開始，mini的index(i)為0，故會符合 i < j的條件，再去判斷如果nums[j] > mini則符合nums[i] < nums[j]的條件，
		# 故要計算兩值相差，並跟maxDiffer比取較大的。最後再判斷目前的mini與nums[j]哪個較小，若nums[j]較小，則下一次的iteration的index(i)會是j，而j會變為j+1
		# 故還是符合 i < j的條件。
		# temination: 終止條件為j = n + 1，且已經檢查完nums[1..n]的所有數，則maxDiff為符合 i<j 並且 nums[i] < nums[j] 的最大相差值。

		n = len(nums)
		maxDiff = -1
		mini = nums[0]

		for j in range(1, n):
			if mini < nums[j]:
				maxDiff = max(maxDiff, nums[j] - mini)
			mini = min(mini, nums[j])

		return maxDiff




	def maximumDifference(self, nums: list[int]) -> int:

		maxDiff = -1

		n = len(nums)

		for i in range(0, n):
			for j in range(i+1, n):
				if i < j and nums[i] < nums[j]:
					maxDiff = max(nums[j] - nums[i], maxDiff)

		return maxDiff
