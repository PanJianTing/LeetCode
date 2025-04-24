from collections import defaultdict

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        cnt_map = defaultdict(int)
        res = 0

        for a in answers:
            if (cnt_map[a] % (a+1)) == 0:
                res += a + 1
            
            cnt_map[a] += 1
        
        return res
    
print(Solution().numRabbits([1,1,2]))