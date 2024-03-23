class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        ans = 0

        def encrypt(num: int) -> int:
            cnt = 0
            max_cnt = 0

            while num > 0:
                max_cnt = max(max_cnt, num % 10)
                num //= 10
                cnt += 1

            res = 0

            for i in range(cnt):
                res += (max_cnt * (10 ** i))
            return res
        
        for n in nums:
            ans += encrypt(n)
        return ans
    
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        ans = 0

        def encrypt(num: int) -> int:
            num_str = str(num)
            N = len(num_str)
            max_cnt = max(num_str)
            return int(max_cnt * N)
        
        for n in nums:
            ans += encrypt(n)
        return ans
    
print(Solution().sumOfEncryptedInt([1, 2, 3]))
print(Solution().sumOfEncryptedInt([10, 21, 31]))