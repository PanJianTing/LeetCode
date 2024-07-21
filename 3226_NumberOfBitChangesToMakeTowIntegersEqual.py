class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        res = 0 
        while n > 0 or k > 0:
            cur_n = n & 1
            cur_k = k & 1

            if cur_n:
                if cur_k == 0:
                    res += 1
            else:
                if cur_k:
                    return -1
            n = n >> 1
            k = k >> 1
        return res
    
    def minChanges(self, n: int, k: int) -> int:
        need_change = n ^ k
        can_change = need_change & n

        change_cnt = bin(need_change).count('1')

        return  change_cnt if change_cnt == bin(can_change).count('1') else -1
    
print(Solution().minChanges(13, 4))
print(Solution().minChanges(21, 21))
print(Solution().minChanges(14, 13))
print(Solution().minChanges(11, 56))


