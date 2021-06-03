
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            return list(reversed(self.decrypt(list(reversed(code)), -k)))
        # brute force
        res = [0] * len(code)
        code2 = code * 2
        # for i in range(len(code)):
        #     res[i] = sum(code2[i+1:i+1+k])
        #
        # accumulative sum
        sums = [0] * len(code2)
        sums[0] = code[0]
        for i in range(1, len(code2)):
            sums[i] = sums[i-1] + code2[i]
        for i in range(len(code)):
            res[i] = sums[i+k] - sums[i]
        return res


    def decrypt_my(self, code: list[int], k: int) -> list[int]:

        length = len(code)
        result = []
        if k == 0:
            return [0] * length

        elif k > 0:

            for i in range(length):
                sum = 0
                for j in range(1, k + 1):
                    sum += code[((i + j) % length)]
                result.append(sum)

            return result
        
        else:

            return self.decrypt(code[::-1], -1*k)[::-1]


Solution.decrypt(Solution(), [5,7,1,4], 3)
