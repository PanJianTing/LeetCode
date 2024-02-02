class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        all_digit = '123456789'

        for cur in range(1, 10):
            for i in range(0, 10):
                if i + cur < 10:
                    cur_num = int(all_digit[i: i+cur])
                    # print(cur_num)
                    if low <= cur_num <= high:
                        ans.append(cur_num)
                    if cur_num > high:
                        return ans

        return ans
    
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        M = len(str(low))
        N = len(str(high))
        all_digit = "123456789"
        ans = []

        for cur in range(M, N+1):
            for i in range(0, 10-cur):
                cur_num = int(all_digit[i:i+cur])
                if low <= cur_num <= high:
                    ans.append(cur_num)

        return ans
    
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        all_possible = []
        all_digit = "123456789"
        ans = []

        for cur in range(2, 10):
            for i in range(0, 10-cur):
                all_possible.append(int(all_digit[i: i+cur]))
        
        for num in all_possible:
            if low <= num <= high:
                ans.append(num)

        return ans


    

print(Solution().sequentialDigits(100, 300))
print(Solution().sequentialDigits(1000, 13000))