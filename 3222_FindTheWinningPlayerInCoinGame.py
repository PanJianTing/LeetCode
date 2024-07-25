class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = 0

        while x > 0 and y >= 4:
            x -= 1
            y -= 4
            turn += 1
        return 'Alice' if turn & 1 else 'Bob'
    
    def losingPlayer(self, x: int, y: int) -> str:
        return 'Alice' if min(x, y//4) & 1 else 'Bob'
    
print(Solution().losingPlayer(2, 7))
print(Solution().losingPlayer(4, 11))