class Solution:
	def checkOnesSegment(self, s: str) -> bool:
		'''
		先在S後面補0，為了避免遇到1001這種案例導致segment沒加到1的問題
		首先，因為第一個字元必為'1'，故從第二個字元開始檢查，則isBeforeIsOne設為True
		在iteraction時，判斷當前字元是否為0，為0則segment加1，並isBeforeIsOne設為False
		當前字元為1，則isBeforeIsOne設為True
		結束為，查找所以的S[1...n]的元素即可。
		return segment == 1
		'''
		s += "0"
		isBeforeIsOne = True
		segment = 0

		for i in range(1, len(s)):
			if s[i] == "1":
				isBeforeIsOne = True
			elif s[i] == "0":
				if isBeforeIsOne:
					segment += 1
					isBeforeIsOne = False

		return segment == 1


	def checkOnesSegment(self, s: str) -> bool:
		'''
		跟上面相似，只是從後面找過來
		將S字串轉換成數字int，透過取得最後一個位元是否為1 or 0(sInt & 1)
		來取得segment的數量。

		init：先將二進制s轉換成十進制sInt，假定last_count(上一次的位元)為0，segment的數量為0
		
		iteraction: 根據sInt & 1 這個判斷是來取得最後一個位元為0 or 1，
		如果為1且上一次的位元為0，則segment+1(因為不再連續了)，且last_count設定為1
		如果為0，則last_count設定為0
		最後在把sInt往右邊移動一個位元(相當於/2)

		termination: sInt為0即終止for loop

		'''
		sInt = int(s, 2)

		last_count = 0
		segment = 0

		while sInt:
			if sInt & 1:
				if last_count == 0:
					segment += 1
				last_count = 1
			else:
				last_count = 0
			sInt >>= 1

		return segment == 1




