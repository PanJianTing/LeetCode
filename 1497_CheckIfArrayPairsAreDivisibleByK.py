from collections import defaultdict

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt_map = defaultdict(int)

        for n in arr:
            cnt_map[n % k] += 1
        
        for n in cnt_map.keys():
            if n == 0 and (cnt_map[n] & 1 == 0):
                continue
                
            pair_n = k - n

            if cnt_map[pair_n] != cnt_map[n]:
                return False

        return True
    
    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt_map = defaultdict(int)

        for n in arr:
            cnt_map[n % k] += 1

        if cnt_map[0] & 1:
            return False
        
        for n in range(1, (k>>1)+1):
            if cnt_map[n] != cnt_map[k - n]:
                return False

        return True


    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt_map = defaultdict(int)

        for n in arr:
            cnt_map[(k + (n % k)) % k] += 1
        
        if cnt_map[0] & 1:
            return False

        for n in range(1, (k>>1) + 1):
            if cnt_map[n] != cnt_map[k-n]:
                return False
            
        return True
    
    def canArrange(self, arr: list[int], k: int) -> bool:
        N = len(arr)
        arr = sorted(arr, key=lambda x: ((k + (x%k)) % k))

        st = 0
        end = N-1

        # find 0
        while st < end:
            if arr[st] % k != 0:
                break
            if arr[st+1] % k != 0:
                return False
            st += 2
        
        while st < end:
            if (arr[st] + arr[end]) % k != 0:
                return False
            st += 1
            end -= 1
        
        return True
        


# print(Solution().canArrange([1,2,3,4,5,6], 7))
print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5))
