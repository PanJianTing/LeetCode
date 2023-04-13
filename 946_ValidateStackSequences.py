class Solution:
    def validateStackSequences(self, pushed: list[int], poped: list[int]) -> bool:
        
        i = 0
        j = 0
        stack = []

        while i < len(pushed):
            stack.append(pushed[i])
            while len(stack) > 0 and stack[-1] == poped[j]:
                    stack.pop()
                    j += 1
            i+=1

        return len(stack) == 0
    
    def validateStackSequences(self, pushed: list[int], poped: list[int]) -> bool:
         
        i = 0
        j = 0
         
        for p in pushed:
            pushed[i] = p
            while i > -1 and pushed[i] == poped[j]:
                 i -= 1
                 j += 1

            i += 1
        return i == 0
    

Solution().validateStackSequences([1,2,3,4,5],[4,5,3,2,1])
Solution().validateStackSequences([1,2,3,4,5],[4,3,5,1,2])
