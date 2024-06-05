class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        N = len(words)
        cnt =  [[0] * N for _ in range(26)]
        res = []

        for i in range(N):
            w = words[i]
            for c in w:
                cnt[ord(c) - ord('a')][i] += 1
        
        for i in range(26):
            c = chr(ord('a') + i)
            cnt_list = cnt[i]
            res.extend([c] * min(cnt_list))

        return res
    

    def commonChars(self, words: list[str]) -> list[str]:
        N = len(words)
        chars = set(words[0])
        res = []

        for c in chars:
            temp = float('inf')
            for w in words:
                temp = min(temp, w.count(c))
            res += [c] * temp

        return res
    

print(Solution().commonChars(["bella","label","roller"]))
print(Solution().commonChars(["cool","lock","cook"]))
print(Solution().commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))
