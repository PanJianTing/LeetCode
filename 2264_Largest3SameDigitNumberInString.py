class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digit_list = [""] * 10
        N = len(num)

        for i in range(0, N-2):
            temp = num[i:i+3]
            digit = num[i]
            if len(set(temp)) == 1:
                digit_list[int(digit)] = temp

        for i in range(9, -1, -1):
            if digit_list[i] != '':
                return digit_list[i]
        
        return ""
    
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        N = len(num)

        for i in range(0, N-2):
            if num[i] == num[i+1] == num[i+2]:
                ans = max(ans, num[i])
        
        return ans * 3
    
print(Solution().largestGoodInteger("6777133339"))
print(Solution().largestGoodInteger("2300019"))
print(Solution().largestGoodInteger("42352338"))

        