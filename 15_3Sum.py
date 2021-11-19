class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0    
            counter[i] += 1

        nums = sorted(counter)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        output = []
        # find answer with no duplicates within combo
        for i in range(len(nums)-1):
            # search range
            twoSum = -nums[i]
            min_half, max_half = twoSum - nums[-1], twoSum / 2
            l = bisect_left(nums, min_half, i + 1)
            r = bisect_left(nums, max_half, l)
            
            for j in nums[l:r]:
                if twoSum - j in counter:
                    output.append([nums[i], j, twoSum - j])

        # find ans with duplicates within combo
        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0, 0, 0])
                elif k != 0 and -2 * k in counter:
                    output.append([k, k, -2 * k])
        return output



class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		res = set()
		dups = set()
		seen = {}

		for i, val1 in enumerate(nums):
			if val1 not in dups:
				dups.add(val1)
				for j, val2 in enumerate(nums[i+1:]):
					diff = -val1 - val2
					if diff in seen and seen[diff] == i:
						res.add(tuple(sorted((val1, val2, diff))))
					seen[val2] = i
		return res




	def threeSum_(self, nums: list[int]) -> list[list[int]]:
		res = []
		nums.sort()

		for i in range(len(nums)):
			# if greater than 0, then behide two numbers sum can not be 0, because nums is sorted, so break it
			if nums[i] > 0:
				break
			# if i == 0 or (i-1 and i) is not equal number, then call twoSum
			if i == 0 or nums[i-1] != nums[i]:
				self.twoSum(nums, i , res)
		return res

	def twoSum(self, nums: list[int], i: int, res: list[List[int]]):
		seen = set()
		j = i + 1
		while j < len(nums):
			diff = -nums[i] - nums[j]
			if diff in seen:
				res.append([nums[i], nums[j], diff])
				# if j and j+1 is equal number then j add by 1
				while j + 1 < len(nums) and nums[j] == nums[j + 1]:
					j += 1
			seen.add(nums[j])
			j += 1




	def threeSum(self, nums: list[int]) -> list[list[int]]:

		ans = set()
		count = len(nums)

		nums = sorted(nums)

		for i in range(0, count - 2):
			j = i + 1
			k = count - 1
			if nums[i] > 0:
				break
			while j < k:
				allSum = nums[i] + nums[j] + nums[k]
				if allSum == 0:
					ans.add((nums[i], nums[j], nums[k]))
					j += 1
					k -= 1
				elif allSum > 0:
					k -= 1
				else:
					j += 1

		return list(ans)