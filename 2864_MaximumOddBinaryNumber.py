class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        count_1 = 0
        for c in s:
            if c == '1':
                count_1 += 1
        count_0 = N - count_1
        return '1' * (count_1-1) + '0' * (count_0 if count_0 > 0 else 0) + '1'
    

    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        s = sorted(s)
        left = 0
        right = N-2
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
    
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        count_1 = s.count('1')
        
        return '1' * (count_1 - 1) + '0' * (N - count_1) + '1'
    

    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        s = list(s)
        left = 0
        right = N-1
        
        while left <= right:
            if s[left] == '1':
                left += 1
            elif s[right] == '0':
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        s[right], s[N-1] = s[N-1], s[right]
        return ''.join(s)
        


        

            
    

print(Solution().maximumOddBinaryNumber('010'))
print(Solution().maximumOddBinaryNumber('0101'))