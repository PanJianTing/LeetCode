class Solution:
	def minTimeToType(self, word: str) -> int:

		now = "a"

		step = 0


		for c in word:
			if c == now:
				step += 1
			else:
				diff = abs(ord(now) - ord(c))
				if diff > 13:
					# 逆時針
					step += abs(diff - 26)
				else:
					# 順時針
					step += diff
				# 打字
				now = c
				step += 1

		return step





		
