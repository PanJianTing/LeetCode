class Solution:
    def largestCombination(self, candidate: list[int]) -> int:
        N = len(candidate)
        bit_set = [0] * 23
        ans = 0

        for i in range(N):
            cur = candidate[i]

            bits = bin(cur)[2:][::-1]

            for i in range(len(bits)):
                if bits[i] == '1':
                    bit_set[i] += 1
        
        for cnt in bit_set:
            ans = max(ans, cnt)

        return ans


    def largestCombination(self, candidate: list[int]) -> int:
        N = len(candidate)
        ans = 0

        for i in range(24):
            mask = 1 << i
            cnt = 0

            for n in candidate:
                if n & mask:
                    cnt += 1

            ans = max(ans, cnt)

        return ans



print(Solution().largestCombination([16,17,71,62,12,24,14]))
print(Solution().largestCombination([8,8]))
print(Solution().largestCombination([16,16,48,71,62,12,24,14,17,18,19,20,10000]))
