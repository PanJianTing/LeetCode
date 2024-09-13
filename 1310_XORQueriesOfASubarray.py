from collections import defaultdict

class Solution:
    def xorQueries(self, arr: list[int], q: list[list[int]]) -> list[int]:
        N = len(q)
        dp = defaultdict(int)
        res = []

        for st, end in q:
            temp = 0
            if (st, end) in dp:
                temp = dp[(st, end)]
            else:
                for i in range(st, end + 1):
                    temp ^= arr[i]
            
            dp[(st, end)] = temp
            res.append(temp)
        return res
    
    def xorQueries(self, arr: list[int], q: list[list[int]]) -> list[int]:
        N = len(arr)
        res = []
        for i in range(1, N):
            arr[i] = arr[i-1] ^ arr[i]
        
        for st, end in q:
            if st == 0:
               res.append(arr[end])
            else:
                res.append(arr[end] ^ arr[st-1])

        return res