class Solution:
	def longestPalindrome(self, s: str) -> str:
		longest = ""
		c = 0

		while c < len(s):
			l = c - 1
			r = c + 1

			while r < len(s) and s[c] == s[r]:
				r += 1
				c += 1

			while l >= 0 and r < len(s):
				if s[l] != s[r]:
					break
				elif s[l] == s[r]:
					l -= 1
					r += 1
			currPali = r - l - 1
			if currPali > len(longest):
				longest = s[l+1:r]

			c += 1
		return longest

	#dp
	# if i == j -> True (simple condition)
	# if abs(i-j) = 1 -> s[j] = s[i] -> True
	# if i != j -> T(i+1,j-1) and s[j] == s[i]
	# O(n^2)
	def longestPalindrome(self, s: str) -> str:
		lens = len(s)
		dp = [[False]*lens for _ in range(lens)]
		start_end = [0,0]
		for i in range(lens-1, -1, -1):
			for j in range(lens-1, -1, -1):
				if i > j:
					break
				if i == j:
					dp[i][j] = True
				elif j-i == 1:
					if s[j] == s[i]:
						dp[i][j] = True
				else:
					if dp[i+1][j-1] and s[i] == s[j]:
						dp[i][j] = True

				if dp[i][j]:
					if j-i > start_end[1] - start_end[0]:
						start_end = [i, j]
		return s[start_end[0]:start_end[1]+1]



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