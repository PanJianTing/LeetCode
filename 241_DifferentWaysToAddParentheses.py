from functools import cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        N = len(expression)

        if N == 0:
            return []
        
        if (N == 1 or N == 2) and expression[0].isdigit():
            return [int(expression)]
        
        res = []
        for i in range(N):
            cur_char = expression[i]

            if cur_char.isdigit():
                continue

            left_part = self.diffWaysToCompute(expression[:i])
            right_part = self.diffWaysToCompute(expression[i+1:])

            for n1 in left_part:
                for n2 in right_part:
                    if cur_char == '+':
                        res.append(n1 + n2)
                    elif cur_char == '-':
                        res.append(n1 - n2)
                    else:
                        res.append(n1 * n2)

        return res
    

    def diffWaysToCompute(self, expression: str) -> list[int]:

        @cache
        def dp(st, end):

            if st == end:
                return [int(expression[st:end+1])]
            
            if end - st == 1 and expression[st].isdigit():
                return [int(expression[st: end+1])]
            
            res = []
            for i in range(st, end+1):
                if expression[i].isdigit():
                    continue

                left_part = dp(st, i-1)
                right_part = dp(i+1, end)

                for n1 in left_part:
                    for n2 in right_part:
                        if expression[i] == '+':
                            res.append(n1 + n2)
                        elif expression[i] == '-':
                            res.append(n1 - n2)
                        else:
                            res.append(n1 * n2)
            
            return res
        
        return dp(0, len(expression)-1)





    

print(Solution().diffWaysToCompute("2-1-1"))
print(Solution().diffWaysToCompute("2*3-4*5"))