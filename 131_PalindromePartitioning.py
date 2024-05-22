class Solution:
    def partition(self, s: str) -> list[list[str]]:
        N = len(s)
        res = []
        def palindrome(st, end):
            while st < end:
                if s[st] != s[end]:
                    return False
                st += 1
                end -= 1
            return True
        
        def dfs(idx, cur_list):
            if idx >= N:
                res.append(cur_list[:])
                return
            
            for end in range(idx, N):
                if palindrome(idx, end):
                    cur_list.append(s[idx : end+1])
                    dfs(end+1, cur_list)
                    cur_list.pop()
        
        dfs(0, [])
        return res
    
    def partition(self, s: str) -> list[list[int]]:
        N = len(s)
        res = []

        dp = [[False] * N for _ in range(N)]

        def dfs(idx, cur_list):
            if idx >= N:
                res.append(cur_list[:])
                return
            for end in range(idx, N):
                if (s[idx] == s[end]) and ((end - idx) <= 2 or dp[idx+1][end-1]):
                    dp[idx][end] = True
                    cur_list.append(s[idx:end+1])
                    dfs(end+1, cur_list)
                    cur_list.pop()
        dfs(0, [])
        return res


print(Solution().partition("aab"))
print(Solution().partition("a"))
