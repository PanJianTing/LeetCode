class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        N = len(currentState)
        ans = []
        
        for i in range(1, N):
            if currentState[i] == "+" and currentState[i-1] == currentState[i]:
                ans.append(currentState[:i-1] + '--' + currentState[i+1:])
        
        return ans
    

    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        N = len(currentState)
        ans = []

        for i in range(N-1):
            if currentState[i] == "+" and currentState[i] == currentState[i+1]:
                ans.append(currentState[:i] + '--' + currentState[i+2:])
        return ans
    
print(Solution().generatePossibleNextMoves("++++"))
print(Solution().generatePossibleNextMoves("+"))
print(Solution().generatePossibleNextMoves("--"))