class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        N = len(nums)
        bit_cnt = [0] * maximumBit
        ans = []

        for n in nums:
            cur_bit = bin(n)[2:][::-1]

            for i in range(len(cur_bit)):
                bit_cnt[i] += int(cur_bit[i])
        
        for i in range(N-1, -1, -1):
            
            k = 0
            for j in range(maximumBit):
                if bit_cnt[j] & 1 == 0:
                    k += (1 << j)
            
            cur_bit = bin(nums[i])[2:][::-1]
            for i in range(len(cur_bit)):
                bit_cnt[i] -= int(cur_bit[i])
            
            ans.append(k)
        
        return ans

    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        N = len(nums)
        prefix_xor = [0] * N
        prefix_xor[0] = nums[0]
        ans = []

        for i in range(1, N):
            prefix_xor[i] = prefix_xor[i-1] ^ nums[i]

        for i in range(N-1, -1, -1):
            cur_xor = prefix_xor[i]

            k = 0
            for j in range(maximumBit):
                if cur_xor & 1 == 0:
                    k += (1 << j)
                cur_xor >>= 1

            ans.append(k)
        return ans
    

    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        N = len(nums)
        all_xor = 0
        ans = []

        for i in range(0, N):
            all_xor ^= nums[i]

        mask = (1 << maximumBit) - 1
        for i in range(N-1, -1, -1):

            ans.append(all_xor ^ mask)
            all_xor ^= nums[i]
        return ans

    
print(Solution().getMaximumXor([0,1,1,3], 2))
                



            