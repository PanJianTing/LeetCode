class Solution:

    def minOperations(self, s: int) -> int:
        
        oddS = s[1::2]
        evenS = s[::2]
        # 由0開頭，0101010101010....
        zeros = evenS.count("0")
        ones = oddS.count("1")

        # 由1開頭，10101010101....
        ones2 = evenS.count("1")
        zeros2 = oddS.count("0")

        odd = len(s) - (ones + zeros)
        even = len(s) - (ones2 + zeros2)

        return min(odd, even)




    def minOperations_my(self, s: str) -> int:

        arrayS = list(s)

        array0 = []
        array1 = []

        diff0 = 0
        diff1 = 0

        start = 0
        for i in range(0, len(arrayS)):
            array0.append(start)
            start = 1 - start

        start = 1
        for i in range(0, len(arrayS)):
            array1.append(start)
            start = 1 - start


        for i in range(0, len(arrayS)):

            count = int(arrayS[i])

            if count != array0[i]:
                diff0 += 1

            if count != array1[i]:
                diff1 += 1

            
        return min(diff1, diff0)
    

    def minOperations(self, s):
        N = len(s)
        ans1 = 0
        ans0 = 0

        for i, c in enumerate(s):
            if i % 2:
                if c == '0':
                    ans1 += 1
                else:
                    ans0 += 1
            else:
                if c == '0':
                    ans0 += 1
                else:
                    ans1 += 1

        return min(ans1, ans0)
    
    def minOperations(self, s):
        N = len(s)
        ans = 0

        for i, c in enumerate(s):
            if i % 2:
                if c == '1':
                    ans += 1
            else:
                if c == '0':
                    ans += 1

        return min(ans, N - ans)
    
    def minOperations(self, s):
        N = len(s)
        curZero = True
        change1 = 0

        for c in s:
            if not (curZero == (c == '0')):
                change1 += 1
                
            curZero = not curZero

        return min(change1, N - change1)


print(Solution().minOperations('0100'))
print(Solution().minOperations('10'))
print(Solution().minOperations('1111'))