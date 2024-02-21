class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        ans = left
        for n in range(left+1, right+1):
            ans &= n
        return ans
    
    # find Prefix common
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        shift = 0
        
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    
    # Brian Kernighan's Algorithm
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        while left < right:
            right = right & (right -1)
        
        return left & right

print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(1, 2147483647))