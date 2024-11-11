class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        N = len(nums)
        prime_list = []

        def check_prime(cur):
            for i in range(2, int((cur ** 0.5))+1):
                if cur % i == 0:
                    return False
            return True
        

        for i in range(max(nums), 1, -1):
            if check_prime(i):
                prime_list.append(i)



        for i in range(N):
            cur_num = nums[i]
            if i == 0:
                for prime in prime_list:
                    if cur_num > prime:
                        nums[i] = cur_num - prime
                        break
            else:
                for prime in prime_list:
                    if cur_num > prime and cur_num-prime > nums[i-1]:
                        nums[i] = cur_num - prime
                        break
                if nums[i] > nums[i-1]:
                    continue
                else:
                    return False
        
        return True
    

    def primeSubOperation(self, nums: list[int]) -> bool:
        N = len(nums)
        
        def check_prime(cur):

            for i in range(2, int(cur ** 0.5)+1):
                if cur % i == 0:
                    return False
            return True

        for i in range(N):
            cur_num = nums[i]

            if i == 0:
                bound = cur_num
            else:
                bound = nums[i] - nums[i-1]
            
            if bound <= 0:
                return False

            for n in range(bound-1, 1, -1):
                if check_prime(n):
                    nums[i] = cur_num - n
                    break
        
        return True
    

    def primeSubOperation(self, nums: list[int]) -> bool:
        N = len(nums)
        max_num = max(nums)
        prime_list = [0] * (max_num+1)

        def check_prime(cur):
            for i in range(2, int(cur ** 0.5)+1):
                if cur % i == 0:
                    return False
                
            return True

        for i in range(2, max_num+1):
            if check_prime(i):
                prime_list[i] = i
            else:
                prime_list[i] = prime_list[i-1]
        
        for i in range(N):
            cur_num = nums[i]

            if i == 0:
                bound = cur_num
            else:
                bound = cur_num - nums[i-1]
            
            if bound <= 0:
                return False
            
            nums[i] = cur_num - prime_list[bound-1]
        
        return True


            




print(Solution().primeSubOperation([4,9,6,10]))
print(Solution().primeSubOperation([5,8,3]))