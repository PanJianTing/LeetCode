class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        M = len(arr1)
        N = len(arr2)
        res = 0

        arr1_str_list = []
        arr2_str_list = []

        for n in arr1:
            arr1_str_list.append(str(n))
        
        for n in arr2:
            arr2_str_list.append(str(n))
    

        for i in range(M):
            n1 = arr1_str_list[i]
            for j in range(N):
                n2 = arr2_str_list[j]
                temp = 0
                for c1, c2 in zip(n1, n2):
                    if c1 == c2:
                        temp += 1
                    else:
                        break
                res = max(temp, res)

        return res
    

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        M = len(arr1)
        N = len(arr2)
        res = 0
        prefix_set = set()

        for i in range(M):
            n = arr1[i]
            while n > 0:
                prefix_set.add(n)
                n //= 10
        
        
        for i in range(N):
            n = arr2[i]
            while n > 0:
                if n in prefix_set:
                    res = max(res, len(str(n)))
                    break
                
                n //= 10

        return res

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        res = 0
        prefix_set = set()
        for n in arr1:
            while n > 0:
                prefix_set.add(n)
                n //= 10
        
        
        for n in arr2:
            while n > 0 and n not in prefix_set:
                n //= 10
            
            if n > 0:
                res = max(res, len(str(n)))

        return res
    

print(Solution().longestCommonPrefix([1,10,100], [1000]))
print(Solution().longestCommonPrefix([1,2,3], [4,4,4]))
                


        