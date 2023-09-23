class Solution:
    def validSubarrays(self, nums) -> int:

        ans = 0
        N = len(nums)

        for i in range(N):
            temp = 1
            leftmost = nums[i]
            for j in range(i+1, N):
                if leftmost <= nums[j]:
                    temp += 1
                else:
                    break
            ans += temp
        
        return ans
    

    def validSubarrays(self, nums) -> int:

        N = len(nums)
        ans = 0
        st = []
        st.append(0)

        for i in range(1, N):
            while st and nums[st[-1]] > nums[i]:
                ans += len(st)
                st.pop()
            
            st.append(i)
        
        while st:
            ans += len(st)
            st.pop()

        return ans
    
    def validSubarrays(self, nums) -> int:

        N = len(nums)
        ans = 0
        st = []
        st.append(0)

        for i in range(1, N):
            while st and nums[st[-1]] > nums[i]:
                ans += i - st[-1]
                st.pop()
            
            st.append(i)
        
        while st:
            ans += N - st[-1]
            st.pop()

        return ans
    
    def validSubarrays(self, nums) -> int:

        N = len(nums)
        ans = 0
        st = []
        st.append(0)
        cur_length = 1

        for i in range(1, N):
            while st and nums[st[-1]] > nums[i]:
                ans += cur_length
                st.pop()
                cur_length -= 1
            
            st.append(i)
            cur_length += 1
        
        while st:
            ans += cur_length
            st.pop()
            cur_length -= 1

        return ans
    

    def validSubarrays(self, nums):
        cur_cnt = 0
        st = []
        ans = 0

        for n in nums:
            while st and st[-1] > n:
                st.pop()
                cur_cnt -= 1
            st.append(n)
            cur_cnt += 1
            ans += cur_cnt
        return ans

#11
print(Solution().validSubarrays([1,4,2,5,3]))

#3
print(Solution().validSubarrays([3,2,1]))

#6
print(Solution().validSubarrays([2,2,2]))

# 20
print(Solution().validSubarrays([15,1,15,20,10,17,19,17]))



        