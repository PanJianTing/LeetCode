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


# 2023/10/27 second

class Solution:
	def longestPalindrome(self, s: str) -> str:
		N = len(s)
		def helper(i, j):
			l = i
			r = j

			while l <= r:
				if s[l] == s[r]:
					l += 1
					r -= 1
				else:
					return False
				
			return True
		
		
		for length in range(N, 0, -1):
			for i in range(0, N-length+1):
				j = i+length-1
				if helper(i, j):
					return s[i:j+1]
		
		return ""
	
	def longestPalindrome(self, s: str) -> str:
		N = len(s)

		dp = [[False] * N for _ in range(N)]

		ans = [0, 0]

		for i in range(N):
			dp[i][i] = True

		for i in range(N-1):
			if s[i] == s[i+1]:
				dp[i][i+1] = True
				ans = [i, i+1]

		for diff in range(2, N):
			for i in range(0, N - diff):
				j = i + diff
				if s[i] == s[j] and dp[i+1][j-1]:
					dp[i][j] = True
					ans[0] = i
					ans[1] = j
		
		return s[ans[0]:ans[1]+1]
	

class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ""
        N = len(s)

        for i in range(0, N):
            for j in range(0, i+1):
                # print(s[j:i+1], s[j:i+1:-1])
                now = s[j:i+1]
                # print("".join(reversed(now)))
                if now == "".join(reversed(now)):
                    if len(s[j:i+1]) > len(ans):
                        ans = s[j:i+1]

        return ans
    
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""
        N = len(s)

        dp = [[""] * (N+1) for _ in range(N+1)]
        revers_s = s[::-1]

        for i in range(0, N):
            for j in range(0, N):
                if s[i] == revers_s[j]:
                    dp[i+1][j+1] += dp[i][j] + s[i]
                    if len(dp[i+1][j+1]) > len(ans):
                        ans = dp[i+1][j+1]
        
        return ans
    
    def longestPalindrome(self, s):

        N = len(s)

        def helper(i, j):
            l = i
            r = j
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1
        
        ans = [0, 0]

        for i in range(N):
            oddL = helper(i, i)
            if oddL > (ans[1] - ans[0] + 1):
                dist = oddL // 2
                ans[0] = i-dist
                ans[1] = i+dist
            
            evenL = helper(i, i+1)
            if evenL > (ans[1] - ans[0] + 1):
                dist = evenL // 2 - 1
                ans[0] = i - dist 
                ans[1] = i + dist + 1

        return s[ans[0]:ans[1]+1]
		

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))

