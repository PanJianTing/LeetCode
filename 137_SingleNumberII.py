from collections import defaultdict

class Solution:
    
    # sol #1 Using Map time -> O(n), space -> O(n)
    def singleNumber(self, nums) -> int:

        cntDict = defaultdict(int)

        for n in nums:
            cntDict[n] += 1
        
        for n in cntDict.keys():
            if cntDict[n] == 1:
                return n
        
        return -1
    
    # sol #2 Sorting Time -> O(nlogn), space -> O(n) 
    def singleNumber(self, nums) -> int:

        N = len(nums)
        nums.sort()

        for i in range(0, N-1, 3):
            if nums[i] == nums[i+1]:
                continue
            else:
                return nums[i]
            
        return nums[-1]
    

    # sol #3 Math Time -> O(n), space -> O(n)
    def singleNumber(self, nums) -> int:

        return (3 * sum(set(nums)) - sum(nums)) >> 1
    
    # sol #4 Bit -> O(32 * n), space -> O(1)
    def singleNumber(self, nums) -> int:

        loner = 0

        for shift in range(32):

            bitsum = 0
            
            for num in nums:
                bitsum += (num >> shift) & 1
            
            loner = loner | ((bitsum % 3) << shift)


        '''
        Python doesn't have fixed-size integers, they are dynamically allocated. 
        The interpreter doesn't know if the answer is constructed in 2's complement or not. 
        In other words, it doesn't know if the leftmost set MSB is a sign bit or a value bit.

        Now, we know that the maximum value of loner is 2^31 - 1. 
        So, if loner turns out to be more than this, it means that the leftmost set bit is a sign bit. 
        So, we need to convert it to 2's complement. We can do this by subtracting 2^32 from loner. 
        
        More can be read https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex.
        '''
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner
    
    # sol #5 *
    def singleNumber(self, nums) -> int:
        one = 0
        two = 0

        for num in nums:
            print(~two)
            one = (one ^ num) & (~two)
            print(~one)
            two = (two ^ num) & (~one)

        return one
    
    # sol #6 *
    def singleNumber(self, nums) -> int:
        return 0
    
Solution().singleNumber([2,2,3,2])
