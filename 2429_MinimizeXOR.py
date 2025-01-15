class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit1_list = []
        bit2_cnt = 0
        ans = 0
        idx = 1

        while num2 > 0:
            if num2 & 1:
                bit2_cnt += 1
            num2 >>= 1
        
        while num1 > 0:
            bit1_list.append(num1 & 1)
            num1 >>= 1
        
        bit1_list = bit1_list[::-1]
        temp_list = [0] * len(bit1_list)

        for i in range(len(bit1_list)):
            cur = bit1_list[i]
            if cur == 1 and bit2_cnt > 0:
                temp_list[i] = 1
                bit2_cnt -= 1
            
        for i in range(len(temp_list)-1, -1, -1):
            if temp_list[i] == 0 and bit2_cnt > 0:
                temp_list[i] = 1
                bit2_cnt -= 1
            
        
        for i in range(bit2_cnt):
            temp_list.append(1)

        
        for i in range(len(temp_list)-1, -1, -1):
            ans += temp_list[i] * idx
            idx <<= 1

        return ans
    
    def minimizeXor(self, num1: int, num2: int) -> int:

        res = num1
        cur_cnt = bin(res).count('1')
        target_cnt = bin(num2).count('1')

        cur_bit_pos = 0

        while cur_cnt < target_cnt:
            if self.isSet(res, cur_bit_pos) == False:
                res = self.setBit(res, cur_bit_pos)
                cur_cnt += 1
            cur_bit_pos += 1
        
        while cur_cnt > target_cnt:
            if self.isSet(res, cur_bit_pos):
                res = self.unsetBit(res, cur_bit_pos)
                cur_cnt -= 1
            cur_bit_pos += 1
        
        return res

    def isSet(self, cnt, bit):
        return (cnt & (1 << bit)) > 0

    def setBit(self, cnt, bit):
        return cnt | (1 << bit)

    def unsetBit(self, cnt, bit):
        return cnt & ~(1 << bit)

# print(Solution().minimizeXor(65, 84))    
# print(Solution().minimizeXor(3, 5))
print(Solution().minimizeXor(12, 1))
