
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


        # 因miss的數在arr[right] ~ arr[left] 之間。
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

print(Solution.findKthPositive(Solution(), [2,3,4,7,11], 5))
print(Solution.findKthPositive(Solution(), [1,2,3,4], 2))
print("Hello World!")