class Solution:
    # in real lift
    def sortArray(self, nums: list[int]) -> list[int]:
        return sorted(nums)

    # merge sort  
    def sortArray(self, nums: list[int]) -> list[int]:
        temp_arr = [0] * len(nums)

        def merge(left: int, mid: int, right: int):

            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            i, j, k = 0, 0, left

            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        def mergeSort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) >> 1

            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            merge(left, mid, right)

        mergeSort(0, len(nums) - 1)
        return nums


    # heap sort
    def sortArray(self, nums: list[int]) -> list[int]:

        def heapify(n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        def heap_sort():
            n = len(nums)

            for i in range(((n >> 1) - 1), -1, -1):
                heapify(n, i)
            
            for i in range(n-1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)

        heap_sort()
        return nums

    # count sort
    def sortArray(self, nums: list[int]) -> list[int]:

        def counting_sort():
            counts = {}
            minVal, maxVal = min(nums), max(nums)

            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index = 0
            for val in range(minVal, maxVal + 1):
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        counting_sort()
        return nums

    # radix sort
    def radix_sort(self, nums: list[int]) -> list[int]:
        max_element = nums[0]

        for val in nums:
            max_element = max(abs(val), max_element)
        
        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10
        
        place_value = 1

        def bucket_sort():
            buckets = [[] for _ in range(10)]

            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        return negatives + positives

    def sortArray(self, nums: list[int]) -> list[int]:

        return self.radix_sort(nums)

        
    
# print(Solution().sortArray([5, 2, 3, 1]))
print(Solution().sortArray([1, -10, 4, 3, -15, 4, 8]))