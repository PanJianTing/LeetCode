from collections import Counter, defaultdict

class Solution:
	def findTheDifference(self, s: str, t: str) -> str:

		diff = 0

		for c in s:
			diff ^= ord(c)

		for c in t:
			diff ^= ord(c)

		return chr(diff)



	def findTheDifference(self, s: str, t: str) -> str:

		return list(Counter(t) - Counter(s))[0]


	def findTheDifference_1(self, s: str, t: str) -> str:

		dic = Counter(s)
		
		for c in t:
			if c not in dic or dic[c] == 0:
				return c
			else:
				dic[c] -= 1

		return ""

	def findTheDifference(self, s: str, t: str) -> str:

		dic = {}

		for c in s:
			if c in dic:
				dic[c] += 1
			else:
				dic[c] = 1

		for c in t:
			if c not in dic or dic[c] == 0:
				return c
			else:
				dic[c] -= 1

		return ""


	def findTheDifference(self, s: str, t: str) -> str:

		dic = {}
		difference = ""

		for c in s:
			if c in dic:
				dic[c] += 1
			else:
				dic[c] = 1

		for c in t:
			if c in dic:
				dic[c] -= 1
				if dic[c] == 0:
					del dic[c]
			else:
				difference += c

		for c in dic.keys():

			difference += c



		return difference
	

class Solution:
    def findTheDifference(self, s, t):
        M = len(s)
        N = len(t)

        s = sorted(s)
        t = sorted(t)

        ps = 0
        pt = 0
        while ps < M and pt < N:
            if s[ps] == t[pt]:
                ps += 1
            else:
                return t[pt]
            pt += 1
        
        return t[pt]
    
    def findTheDifference(self, s: str, t: str) -> str:
        t_dic = defaultdict(int)

        for c in t:
            t_dic[c] += 1

        for c in s:
            t_dic[c] -= 1

        for key, val in t_dic.items():
            if val:
                return key
        return t[0]
    
    def findTheDifference(self, s, t):
        s_dic = defaultdict(int)

        for c in s:
            s_dic[c] += 1
        
        for c in t:
            s_dic[c] -= 1
            if s_dic[c] < 0:
                return c
            
    def findTheDifference(self, s, t):
        ans = 0
        
        for c in s:
            ans ^= ord(c)
        
        for c in t:
            ans ^= ord(c)
        
        return chr(ans)
    
    
print(Solution().findTheDifference("abcd", "abcde"))
print(Solution().findTheDifference("", "y"))