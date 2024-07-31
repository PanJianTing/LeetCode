from functools import cache

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        N = len(books)

        @cache
        def dp(cur_idx, cur_width, cur_h):
            if cur_idx == N:
                return cur_h
            
            if books[cur_idx][0] + cur_width <= shelfWidth:
                return min(dp(cur_idx + 1, cur_width + books[cur_idx][0], max(books[cur_idx][1], cur_h)), 
                           cur_h + dp(cur_idx + 1, books[cur_idx][0], books[cur_idx][1]))
            return cur_h + dp(cur_idx + 1, books[cur_idx][0], books[cur_idx][1])

        return dp(0, 0, 0)
    

    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        N = len(books)
        dp = [0] * (N+1)

        dp[1] = books[0][1]

        for i in range(2, N+1):
            dp[i] = books[i-1][1] + dp[i-1]

            j = i-1
            cur_h = books[j][1]
            cur_w = books[j][0]
            while j > 0 and cur_w + books[j-1][0] <= shelfWidth:
                cur_h = max(cur_h, books[j-1][1])
                cur_w += books[j-1][0]
                dp[i] = min(dp[i], cur_h + dp[j-1])
                j -= 1
            
        return dp[N]


print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
print(Solution().minHeightShelves([[1,3],[2,4],[3,2]], 6))
