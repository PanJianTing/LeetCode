class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        total = 0
        level = 1
        cur_num = 2
        while total < k:
            total += cur_num
            cur_num <<= 1
            level += 1

        level_list = [""]
        cur = 0
        for _ in range(level-1):
            temp = []
            N = len(level_list)
            for i in range(N):
                for s in ["4", "7"]:
                    temp.append(level_list[i] + s)
                    cur += 1
                    if cur == k:
                        return temp[-1]
            level_list = temp


    def kthLuckyNumber(self, k: int) -> str:
        c = 0
        cur = 1
        total = 0
        res = ""
        while total < k:
            cur = cur << 1
            total += cur
            c += 1

        x = k - (total - (2 ** (c))) - 1

        while c > 0:
            if x & 1:
                res = '7' + res
            else:
                res = '4' + res
            x >>= 1
            c -= 1
            
        return res


    def kthLuckyNumber(self, k: int) -> str:
        k = k+1
        bit_list = []

        while k > 0:
            bit_list.append(k%2)
            k >>= 1
        
        bit_list.pop()
        res = ""

        for i in range(len(bit_list)-1, -1, -1):
            if bit_list[i]:
                res += '7'
            else:
                res += '4'
        return res
    
    def kthLuckyNumber(self, k: int) -> str:
        k = k+1
        res = ''

        while k > 1:
            if k & 1:
                res = "7" + res
            else:
                res = '4' + res
            k >>= 1
        return res
    

    def kthLuckyNumber(self, k: int) -> str:
        k = k+1
        # print(bin(k))
        res = bin(k)[3:]
        return res.replace('0', '4').replace('1', '7')


            


print(Solution().kthLuckyNumber(4))
print(Solution().kthLuckyNumber(10))
print(Solution().kthLuckyNumber(1000))
print(Solution().kthLuckyNumber(10000))

