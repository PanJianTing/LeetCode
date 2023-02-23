class Solution:
    def countOdds(self, low: int, high: int) -> int:

        result = (high - low) // 2

        if (low % 2) == 1 or (high % 2) == 1:
            result += 1
        return result
    
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0

        if low % 2:
            count += 1
        elif high % 2:
            count += 1
        return (high - low) // 2 + count
    
    def countOdds(self, low: int, high: int) -> int:

        return (high - low) // 2 + (low % 2 or high % 2)

    def countOdds(self, low: int, high: int) -> int:

        return ((high + 1) >> 1) - (low >> 1)