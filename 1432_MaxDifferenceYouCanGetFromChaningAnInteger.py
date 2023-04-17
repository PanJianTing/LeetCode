class Solution:
    def maxDiff(self, num: int) -> int:

        A = []
        while num > 0:
            A.append(num%10)
            num //= 10
        A.reverse()
        # print(A)

        pickMax = A[0]
        for c in A:
            if c != 9:
                pickMax = c
                break
        
        pickMin = A[0]
        for c in A:
            if c != 1 and c != 0:
                pickMin = c
                break

        a = 0
        b = 0
        for i, c in enumerate(reversed(A)):
            index = 10**i
            if c == pickMax:
                a += 9 * index
            else:
                a += c * index

            if c == pickMin:
                if c == A[0]:
                    b += 1 * index
                else:
                    b += 0 * index
            else:
                b += c * index

        return a-b
    
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNum = float('-inf')
        minNum = float('inf')

        for i in '0123456789':
            for j in '0123456789':
                nextNum = num.replace(i, j)
                if nextNum[0] == '0' or int(nextNum) == 0:
                    continue
                maxNum = max(maxNum, int(nextNum))
                minNum = min(minNum, int(nextNum))

        return maxNum - minNum
    
    def maxDiff(self, num: int) -> int:
        A = B = str(num)

        # findMax
        for a in A:
            if a != '9':
                A = A.replace(a, '9')
                break
        
        # findMin
        if B[0] == '1':
            for b in B:
                if b != '0' and b != '1':
                    B = B.replace(b, '0')
                    break
        else:
            B = B.replace(B[0], '1')

        return int(A) - int(B)



    
print(Solution().maxDiff(555))
print(Solution().maxDiff(9288))
print(Solution().maxDiff(123456))