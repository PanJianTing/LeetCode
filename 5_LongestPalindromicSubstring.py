class Solution:
	def longestPalindrome(self, s: str) -> str:

		nums = len(s)

		for count in range(nums, 0, -1):
			start = 0

			while start + count <= nums:
				
				subStr = s[start:start+count]

				if subStr == subStr[::-1]:
					return subStr
					
				start += 1

		return s