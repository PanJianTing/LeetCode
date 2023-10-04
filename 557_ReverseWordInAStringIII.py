class Solution:
    def reverseWords(self, s):
        ss = s.split(" ")
        ans = []
        for s in ss:
            ans.append(s[::-1])

        return " ".join(ans)

print(Solution().reversWords("Let's take LeetCode contest"))
print(Solution().reversWords("God Ding"))