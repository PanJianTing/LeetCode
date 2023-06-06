class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:

        arr = sorted(arr)
        diff = set()
        N = len(arr)

        for i in range(1, N):
            diff.add(arr[i] - arr[i-1])

        return len(diff) == 1
    

    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        N = len(arr)

        for i in range(2, N):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
    
    # use set to detect duplicate
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        minV = min(arr)
        maxV = max(arr)
        N = len(arr)

        if maxV - minV == 0:
            return True
        
        if (maxV - minV) % (N-1):
            return False
        
        diff = (maxV - minV) / (N-1)
        numSet = set()

        for num in arr:
            if ((num - minV) % diff):
                return False
            numSet.add(num)

        return len(numSet) == N
    
    # use in-place to check
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        minV = min(arr)
        maxV = max(arr)
        N = len(arr)

        if maxV - minV == 0:
            return True
        
        if (maxV - minV) % (N - 1):
            return False
        
        diff = (maxV - minV) // (N - 1)
        i = 0

        while i < N:
            if (arr[i] == minV + i * diff):
                i += 1
            
            elif (arr[i] - minV) % diff:
                return False
            else:
                j = (arr[i] - minV) // diff

                # check duplicate
                if arr[i] == arr[j]:
                    return False
                
                arr[i], arr[j] = arr[j], arr[i]

        return True
