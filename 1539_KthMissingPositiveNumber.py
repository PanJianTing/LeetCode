
class Solution:

    def findKthPositive(self, arr: list[int], k: int) -> int:

        left = 0
        right = len(arr) -1

        while left <= right:

            mid = (left + right) // 2

            miss = arr[mid] - (mid + 1)

            if miss < k:
                left = mid + 1
                
            else:
                right = mid - 1


        # 因miss的數在arr[right] ~ arr[left] 之間。
        # 先找arr[right]之前缺少幾個數 => (arr[right] - (right + 1)) => arr[right] - right - 1 
        # 然後 k 再減去少掉的數 => k - (arr[right] - right -1)
        # 然後在加上 arr[right] => arr[right] + (k - (arr[right] - right - 1))
        # 化簡 => arr[right] + k - ( arr[right] - right -1 ) => arr[right] + k - arr[right] + right + 1
        # => k + right + 1 => k + left
        return left + k
            


    def findKthPositive_sol1(self, arr: list[int], k: int) -> int:
        
        k -= arr[0] - 1

        if k < 0:
            return k
        
        for i in range(0, len(arr) - 1):
            miss = arr[i+1] - arr[i] - 1
            if miss < k:
                k -= miss
            else:
                return arr[i] + k
        return arr[-1] + k



    def findKthPositive_my(self, arr: list[int], k: int) -> int:
        
        miss = 0
        arrIndex = 0
        findCount = 1

        while k != 0:
            if arrIndex < len(arr) and findCount == arr[arrIndex]:
                arrIndex += 1
            else:
                miss = findCount
                k -= 1
            findCount += 1

        return miss

# 2023/03/06 again
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) >> 1

            diff = arr[mid] - (mid + 1)

            if diff < k:
                left = mid + 1
            else:
                right = mid

        diff = k - (arr[left] - left)
        if diff >= 0:
            diff += 1
        
        return arr[left] + diff
    
    # O(n)
    def findKthPositive(self, arr: list[int], k: int) -> int:

        arrIndex = 0
        now = 1
        miss = []

        while k > 0:

            if arrIndex < len(arr):

                if arr[arrIndex] == now:
                    arrIndex += 1
                    now += 1
                    continue

            miss.append(now)
            now += 1
            k -= 1

        return miss[-1]
    

    # O(n)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        
        if k < arr[0]:
            return k
        k -= arr[0] - 1

        for i in range(1, len(arr)):
            miss = arr[i] - (arr[i-1] + 1)

            if miss < k:
                k -= miss
            else:
                return arr[i-1] + k
            
        return arr[-1] + k
    

    def findKthPositive(self, arr: list[int], k: int) -> int:

        left = 0
        right = len(arr) - 1

        while left <= right:
            pivot = left + ((right - left) >> 1)

            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1


        # arr[right] + (k - (arr[right] - (right+1)))
        # = arr[right] + k - arr[right] + right + 1
        # = k + (right + 1)
        # = k + left (because right = left + 1)

        return k + left

print(Solution().findKthPositive([2,3,4,7,11], 5))  #9
print(Solution().findKthPositive([1,2,3,4], 2))     #6
print(Solution().findKthPositive([3,4,5,6,7], 2))   #2
print(Solution().findKthPositive([5,6,7,8,9], 9))   #14
print(Solution().findKthPositive([1,2], 1))         #3
print("Hello World!")