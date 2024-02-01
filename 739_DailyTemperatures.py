class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        N = len(t)
        ans = [0] * N

        for i in range(N):
            for j in range(i+1, N):
                if t[j] > t[i]:
                    ans[i] = j-i
                    break
        return ans
    
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        N = len(t)
        ans = [0] * N
        st = []

        for i in range(N):
            while st and st[-1][0] < t[i]:
                _, idx = st.pop()
                ans[idx] = i - idx
            st.append([t[i], i])
        return ans
    
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        N = len(t)
        ans = [0] * N
        st = []

        for i in range(N):
            while st and t[st[-1]] < t[i]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans
    
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))