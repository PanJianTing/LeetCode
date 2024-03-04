class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        N = len(tokens)
        tokens.sort()
        left = 0
        right = N-1
        cur_score = 0
        ans = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur_score += 1
                left += 1
            else:
                if cur_score > 0:
                    power += tokens[right]
                    cur_score -= 1
                    right -= 1
                else:
                    break
            
            ans = max(ans, cur_score)

        return ans
    
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        N = len(tokens)
        tokens.sort()
        left = 0
        right = N-1
        cur_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur_score += 1
                left += 1
            else:
                if left < right and cur_score > 0:
                    power += tokens[right]
                    cur_score -= 1
                    right -= 1
                else:
                    break

        return cur_score
    

print(Solution().bagOfTokensScore([100], 50))
print(Solution().bagOfTokensScore([200,100], 150))
print(Solution().bagOfTokensScore([100,200,300,400], 200))