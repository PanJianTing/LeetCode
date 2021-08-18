class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        i = 1
        n = len(sequence)
        k = len(word)
        max = 0

        while i < (n/k + 1):
            try:
                sequence.index(i * word)
            except:
                break
            max = i
            i += 1
        return max




    def maxRepeating_my(sefl, sequence: str, word: str) -> int:
        
        result = 0
        repeatWord = word

        while len(sequence) >= len(repeatWord):
            if repeatWord in sequence:
                result += 1
            repeatWord += word
        return result


Solution.maxRepeating(Solution(), "aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")

"aaabaaaabaaabaaaabaaaabaaaabaaaaba"
"aaaba"