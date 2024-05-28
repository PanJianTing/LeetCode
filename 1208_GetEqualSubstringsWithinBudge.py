class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = 0

        costs = [0] * N

        for i in range(N):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        
        l = 0
        cur_cost = 0

        for r in range(N):

            cur_cost += costs[r]
            while cur_cost > maxCost:
                cur_cost -= costs[l]
                l += 1
            
            res = max(res, r-l+1)

        return res
    

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = 0
        cur_cost = 0
        l = 0
        for r in range(N):
            cur_cost += abs(ord(t[r]) - ord(s[r]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(t[l]) - ord(s[l]))
                l += 1
            res = max(res, r-l+1)
        return res
    
# print(Solution().equalSubstring('abcd', 'bcdf', 3))
# print(Solution().equalSubstring('abcd', 'cdef', 3))
# print(Solution().equalSubstring('abcd', 'acde', 0))
print(Solution().equalSubstring('abcd', 'bcde', 0))