class Solution:
	def maxArea(self, height: list[int]) -> int:

		left = 0
		right = len(height)-1

		maxArea = 0

		while left < right:
			area = (right - left) * min(height[left], height[right])

			if maxArea < area:
				maxArea = area

			if height[left] > height[right]:
				right -= 1
			else:
				left += 1


		return maxArea

	def maxArea(self, height: list[int]) -> int:

		maxHeight = 0
		maxIndex = 0
		maxArea = 0

		for i in range(0, len(height)):
			for j in range(i, len(height)):
				h = min(height[i], height[j])
				between = j - i
				area = h * between
				if maxArea < area:
					maxArea = area

		return maxArea
