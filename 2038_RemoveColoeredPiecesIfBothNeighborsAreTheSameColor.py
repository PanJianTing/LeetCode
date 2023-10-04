class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        N = len(colors)

        for i in range(1, N-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    a += 1
                else:
                    b += 1
        return a > b
    
    def winnerOfGame(self, colors):
        a = 0
        b = 0
        N = len(colors)
        
        for c in "AB":
            while c * 3 in colors:
                colors = colors.replace(c*3, c*2)
                if c == "A":
                    a += (N - len(colors))
                else:
                    b += (N - len(colors))
                N = len(colors)
        
        return a > b

    
print(Solution().winnerOfGame("AAAAABBBBBBAAAAA"))
print(Solution().winnerOfGame("AAABABB"))
print(Solution().winnerOfGame("AA"))
print(Solution().winnerOfGame("ABBBBBBBAAA"))