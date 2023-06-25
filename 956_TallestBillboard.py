class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        
        def backtrack(index, sum1, sum2, left, right):
            print(left, right)
            if index == len(rods):
                if sum1 == sum2:
                    return sum2
                else:
                    return 0
                
            max_h = backtrack(index+1, sum1 + rods[index], sum2, left, right)

            max_h = max(max_h, backtrack(index+1, sum1, sum2+ rods[index], left, right.append(rods[index])))

            max_h = max(max_h, backtrack(index+1, sum1, sum2, left, right))
            
            return max_h
        return backtrack(0,0,0, [], [])
    
Solution().tallestBillboard([1,2])
