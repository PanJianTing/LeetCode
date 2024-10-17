class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = []
        ans = num

        while num > 0:
            digit.append(num % 10)
            num //= 10
        
        N = len(digit)
        for i in range(N-1, 0, -1):
            for j in range(i-1, -1, -1):
                digit[i], digit[j] = digit[j], digit[i]
                temp = 0
                cur = 1
                for k in range(N):
                    temp += digit[k] * cur
                    cur *= 10
                ans = max(ans, temp)
                digit[i], digit[j] = digit[j], digit[i]
        
        return ans
    

    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        N = len(num_str)
        max_right_idx = [0] * N

        max_right_idx[N-1] = N-1

        for i in range(N-2, -1, -1):
            if num_str[i] > num_str[max_right_idx[i+1]]:
                max_right_idx[i] = i
            else:
                max_right_idx[i] = max_right_idx[i+1]
        
        for i in range(N):
            if num_str[i] < num_str[max_right_idx[i]]:
                num_str[i], num_str[max_right_idx[i]] = num_str[max_right_idx[i]], num_str[i]
                return int(''.join(num_str))
            
        return num



print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(98368))
print(Solution().maximumSwap(1993))

