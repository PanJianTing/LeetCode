class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
        remove_set = {'a', 'e', 'i', 'o', 'u'}

        for c in s:
            if c in remove_set:
                continue
            else:
                res.append(c)
        return ''.join(res)