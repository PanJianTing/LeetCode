class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        N = len(derived)

        origin = [0] * N
        checkZero = False
        checkOne = False

        for i in range(1, N):
            origin[i] = origin[i-1] ^ derived[i-1]
        
        checkZero = (derived[N-1] == (origin[N-1] ^ origin[0]))

        origin = [1] * N
        for i in range(1, N):
            origin[i] = origin[i-1] ^ derived[i-1]
        
        checkOne = (derived[N-1] == (origin[N-1] ^ origin[0]))

        return checkZero | checkOne
    

    def doesValidArrayExist(self, derived: list[int]) -> bool:
        all_XOR = 0

        for n in derived:
            all_XOR ^= n
        
        return all_XOR == 0
    

    def doesValidArrayExist(self, derived: list[int]) -> bool:
        cnt = 0

        for n in derived:
            cnt += (1 if n == 1 else 0)

        return cnt & 1 == False