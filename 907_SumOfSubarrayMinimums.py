class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        cur = 0
        res = 0

        for i in range(N):
            for j in range(i, N):
                if i == j:
                    cur = arr[j]
                else:
                    cur = min(cur, arr[j])
                res += cur
        
        return res % MOD
    

    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        st = []
        ans = 0

        for i in range(N):
            cur = arr[i]

            while st and arr[st[-1]] >= cur:
                curIdx = st.pop()
                if st:
                    ans += arr[curIdx] * (i-curIdx) * (curIdx - st[-1])
                else:
                    ans += arr[curIdx] * (i-curIdx) * (curIdx + 1)
            st.append(i)
        
        while st:
            curIdx = st.pop()
            if st:
                ans += arr[curIdx] * (N-curIdx) * (curIdx - st[-1])
            else:
                ans += arr[curIdx] * (N-curIdx) * (curIdx + 1)

        return ans % MOD
    
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        st = []
        res = 0

        for i in range(N+1):

            while st and (i == N or arr[st[-1]] >= arr[i]):

                curIdx = st.pop()
                if st:
                    res += arr[curIdx] * (i - curIdx) * (curIdx - st[-1])
                else:
                    res += arr[curIdx] * (i - curIdx) * (curIdx + 1)
            st.append(i)

        return res % MOD
    
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        dp = [0] * N
        st = [0]

        dp[0] = arr[0]

        for i in range(1, N):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            if st:
                dp[i] = dp[st[-1]] + (arr[i] * (i-st[-1]))
            else:
                dp[i] = arr[i] * (i+1)
            st.append(i)
        
        return sum(dp) % MOD

    
print(Solution().sumSubarrayMins([3,1,2,4]))
print(Solution().sumSubarrayMins([11,81,94,43,3]))
print(Solution().sumSubarrayMins([8,6,3,5,4,9,2]))

