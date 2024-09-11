class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        st = []
        end = []
        res = 0

        while start > 0 or goal > 0:
            st.append(start % 2)
            end.append(goal % 2)
            start >>= 1
            goal >>= 1
        
        for s, e in zip(st, end):
            if s != e:
                res += 1
        return res
    

    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        while start > 0 or goal > 0:
            if (start & 1) != (goal & 1):
                res += 1
            start >>= 1
            goal >>= 1
        return res
    

    def minBitFlips(self, start: int, goal: int) -> int:

        if start == 0 and goal == 0:
            return 0
        
        return (1 if (start & 1) != (goal & 1) else 0) + self.minBitFlips(start >> 1, goal >> 1)
    

    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        res = 0

        while xor > 0:
            res += (xor & 1)
            xor >>= 1
        
        return res

    


print(Solution().minBitFlips(10, 7))

        