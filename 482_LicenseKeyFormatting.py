class Solution:

	def licenseKeyFormatting(self, s: str, k: int) -> str:

		s = s.replace("-", "").upper()[::-1]

		return "-".join(s[a:a+k] for a in range(0, len(s), k))[::-1]


	def licenseKeyFormatting_my(self, s: str, k: int) -> str:

		s = s.replace("-", "").upper()

		i = 0

		fix = len(s)%k

		licenseStr = ""

		if fix != 0:
			licenseStr = s[i:fix] + "-"
			i += fix

		while i < len(s):
			licenseStr += s[i:i+k] + "-"
			i += k

		return licenseStr[:-1]