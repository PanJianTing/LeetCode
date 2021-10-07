class Solution:
	def countTriples(self, n: int) -> int:

		ans = 0
		squareSet = set()

		for i in range(1, n+1):
			squareSet.add(i*i)

		for a in range(1, n):
			for b in range(a, n):
				if a*a + b*b in squareSet:
					ans += 1

		return ans*2



#需查看
class Solution:
    def countTriples(self, n: int) -> int:

        p_max = int((n-1)**0.5)
        count = 0
        for p in range(1,p_max):
            threshold = int((n-p**2)**0.5)
            for s in range(p+1,threshold+1):
                a = 2*p*s
                b = s**2 - p**2
                if gcd(a,b) == 1:
                    c = int((a**2+b**2)**0.5)
                    count += n//c
        
        return count*2