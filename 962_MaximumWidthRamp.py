import heapq

class Solution:
    def maxWidthRamp(self, A: list[int]) -> int:
        hq = []
        ans = 0
        idx = len(A)

        for i, n in enumerate(A):
            heapq.heappush(hq, (n, i))
        

        while hq:
            _, cur_idx = heapq.heappop(hq)

            if cur_idx > idx:
                ans = max(ans, cur_idx - idx)

            idx = min(idx, cur_idx)
        return ans
    
    def maxWidthRamp(self, A: list[int]) -> int:
        N = len(A)
        ans = 0

        for i in range(N):
            for j in range(i+1, N):
                if A[j] >= A[i]:
                    ans = max(ans, j - i)
        
        return ans
    
    def maxWidthRamp(self, A: list[int]) -> int:
        N = len(A)
        indices = [i for i in range(N)]

        indices.sort(key= lambda i: (A[i], i))

        min_index = N
        ans = 0

        for idx in indices:
            ans = max(ans, idx - min_index)
            min_index = min(min_index, idx)
        
        return ans
    

    def maxWidthRamp(self, A: list[int]) -> int:
        N = len(A)
        right_max = [A[N-1]] * N
        l = 0
        r = 0
        res = 0
        for i in range(N-2, -1, -1):
            right_max[i] = max(A[i], right_max[i+1])
        
        while r < N:

            while l < r and A[l] > right_max[r]:
                l += 1
            res = max(res, r-l)
            r += 1
        
        return res
    
    def maxWidthRamp(self, A: list[int]) -> int:
        N = len(A)
        res = 0
        st = []
        st.append(0)

        for i in range(1, N):
            if A[st[-1]] > A[i]:
                st.append(i)

        for i in range(N-1, -1, -1):

            while st and A[st[-1]] <= A[i]:
                res = max(res, i - st.pop())
        
        return res


print(Solution().maxWidthRamp([6,0,8,2,1,5]))
print(Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
