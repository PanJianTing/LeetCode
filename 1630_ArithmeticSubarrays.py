class Solution:
    def checkArithmeticSubarrays(self, nums, l, r) -> list[bool]:
        ans = []

        for i, j in zip(l, r):
            temp = nums[i:j+1]
            temp.sort()

            is_arithmetic = True
            check_cnt = temp[1] - temp[0]
            for k in range(1, len(temp)):
                if temp[k] - temp[k-1] != check_cnt:
                    is_arithmetic = False
                    break

            ans.append(is_arithmetic)

        return ans
    

    def checkArithmeticSubarrays(self, nums, l, r) -> list[bool]:
        
        ans = []
        for i, j in zip(l, r):
            temp = nums[i:j+1]
            max_num = max(temp)
            min_num = min(temp)
            
            
            if max_num == min_num:
                ans.append(True)
            elif (max_num - min_num) % (j-i):
                ans.append(False)
            else:
                temp_set = set(temp)
                d = (max_num - min_num) // (j-i)
                cur = min_num + d
                check_res = True
                for num in range(min_num, max_num, d):
                    if num not in temp_set:
                        check_res = False
                        break
                    cur += d
                ans.append(check_res)
        return ans
    
    def check(self, arr) -> bool:
        arr.sort()
        dif = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != dif:
                return False
        return True
    
    def check(self, arr) -> bool:
        N = len(arr)
        min_val = min(arr)
        max_val = max(arr)
        num_set = set(arr)

        if (max_val - min_val) % (N - 1) != 0:
            return False

        diff = (max_val - min_val) // (N - 1)
        cur = min_val + diff
        while cur < max_val:
            if cur not in num_set:
                return False
            cur += diff
        return True
    
    def checkArithmeticSubarrays(self, arr, l, r) -> list[bool]:
        ans = []
        for i, j in zip(l, r):
            ans.append(self.check(arr[i:j+1]))
        return ans
    
    




#[true,true,true,true,false,true,true,true,true]
print(Solution().checkArithmeticSubarrays([-3,-6,-8,-4,-2,-8,-6,0,0,0,0], [5,4,3,2,4,7,6,1,7], [6,5,6,3,7,10,7,4,10]))
print(Solution().checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
print(Solution().checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))