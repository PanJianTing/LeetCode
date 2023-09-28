class Solution:
    def sortArrayByParity(self, nums) -> list[int]:

        odd = []
        even = []

        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        
        return even + odd
    

    def sortArrayByParity(self, nums):

        N = len(nums)
        ans = [0] * N
        st = 0
        end = N-1

        for n in nums:
            if n % 2:
                ans[end] = n
                end -= 1
            else:
                ans[st] = n
                st += 1
        
        return ans
    
    def sortArrayByParity(self, nums):
        N = len(nums)
        st = 0
        end = len(nums) - 1


        while st < end:

            while st < N and nums[st] % 2 == 0:
                st += 1
            
            while end > 0 and nums[end] % 2 and end > 0:
                end -= 1
            
            if st < end:
                nums[st], nums[end] = nums[end], nums[st]

        return nums
    
    def sortArrayByParity(self, nums):
        N = len(nums)
        st = 0
        end = N - 1

        while st < end:
            if nums[st] % 2:
                if nums[end] % 2 == 0:
                    nums[st], nums[end] = nums[end], nums[st]
                    st += 1
                    end -= 1
                else:
                    end -= 1
            else:
                st += 1
        return nums
    
    def sortArrayByParity(self, nums):
        return sorted(nums, key = lambda x: x%2)
    
    def sortArrayByParity(self, nums):
        return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2]
    
    def sortArrayByParity(self, nums):
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2:
                j -= 1
        
        return nums



    
print(Solution().sortArrayByParity([3,1,2,4]))
print(Solution().sortArrayByParity([0]))
print(Solution().sortArrayByParity([0,2]))

