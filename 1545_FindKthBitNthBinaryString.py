class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cur = '0'

        for _ in range(n-1):
            temp = []
            for c in cur:
                temp.append('1' if c == '0' else '0')
            
            temp = ''.join(temp[::-1])
            cur = cur + '1' + temp
        
        return cur[k-1]
    

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        length = 1 << n
        if k < length // 2:
            return self.findKthBit(n-1, k)
        elif k == length // 2:
            return '1'
        else:
            return '1' if self.findKthBit(n-1, length - k) == '0' else '0'

print(Solution().findKthBit(3, 1))
print(Solution().findKthBit(4, 11))
            
