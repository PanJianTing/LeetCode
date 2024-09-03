class Solution:
    def getLucky(self, s: str, k: int) -> int:
        N = len(s)
        num_list = []
        res = 0

        for c in s:
            num_list.append(str((ord(c) - ord('a')) + 1))
        
        cur_num_str = ''.join(num_list)

        for c in cur_num_str:
            res += int(c)
        k -= 1
        while k > 0:
            if res < 10:
                break
            temp = 0
            while res > 0:
                temp += res % 10
                res //= 10

            res = temp
            k -= 1
        return res
    
    def getLucky(self, s: str, k: int) -> int:
        N = len(s)
        res = 0
        cur_num_str = ''

        for c in s:
            cur_num_str += str((ord(c) - ord('a')) + 1)

        res = int(cur_num_str)
        while k > 0:
            if len(cur_num_str) < 2:
                break
            temp_sum = 0
            for c in cur_num_str:
                temp_sum += int(c)
            
            res = temp_sum
            cur_num_str = str(temp_sum)
            k -= 1
        return res
    
    def getLucky(self, s: str, k: int) -> int:
        res = 0

        for c in s:
            c_num = ord(c) - ord('a') + 1
            res += (c_num // 10 + c_num % 10)
        k -= 1
        while k > 0:
            if res < 10:
                return res
            temp_sum = 0
            while res > 0:
                temp_sum += (res % 10)
                res //= 10
            
            res = temp_sum
            k -= 1
        return res
    

print(Solution().getLucky('iiii', 1))
print(Solution().getLucky('leetcode', 2))
print(Solution().getLucky('zbax', 2))