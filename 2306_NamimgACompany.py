class Solution:
    def distinctNames(self, ideas: list[str]) -> int:

        group = [set() for _ in range(26)]
        for word in ideas:
            group[ord(word[0]) - ord('a')].add(word[1:])
        
        ans = 0
        for i in range(0, 26):
            for j in range(i+1, 26):
                sameNum = len(group[i] & group[j])

                ans += 2 * (len(group[i]) - sameNum) * (len(group[j]) - sameNum)

        return ans

        



print(Solution().distinctNames(["coffee","donuts","time","toffee"]))