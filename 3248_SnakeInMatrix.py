class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        res = 0
        for c in commands:
            if c == "UP":
                res -= n
            elif c == "DOWN":
                res += n
            elif c == "RIGHT":
                res += 1
            else:
                res -= 1
        return res