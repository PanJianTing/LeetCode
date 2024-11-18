class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        if k == 0:
            return [0] * N

        ans = []
        check_code = list(code)
        if k < 0:
            check_code = code[::-1]
        
        for i in range(N):
            cur_sum = 0
            for j in range(i+1, i+abs(k)+1):
                cur_sum += check_code[j % N]
            ans.append(cur_sum)

        return ans if k > 0 else ans[::-1]
    

    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)

        if k == 0:
            return [0] * N
        
        ans = []

        for i in range(N):
            cur_sum = 0
            if k > 0:
                for j in range(i+1, i+k+1):
                    cur_sum += code[j % N]
            else:
                for j in range(i-(-k), i):
                    cur_sum += code[j]
            ans.append(cur_sum)
        return ans
    

    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)

        if k == 0:
            return [0] * N
        ans = []
        cur_sum = 0
        st = 0
        end = 0

        if k > 0:
            st = 1
            for i in range(1, k+1):
                cur_sum += code[i]
                end = i
        else:
            st = N-(-k)
            for i in range(N - (-k), N):
                cur_sum += code[i]
                end = i

        ans.append(cur_sum)

        for i in range(1, N):
            cur_sum -= code[st % N]
            cur_sum += code[(end + 1) % N]
            st += 1
            end += 1
            ans.append(cur_sum)
        
        return ans
    
# print(Solution().decrypt([5,7,1,4], 3))
# print(Solution().decrypt([2,4,9,3], -2))
print(Solution().decrypt([10,5,7,7,3,2,10,3,6,9,1,6], -4))

