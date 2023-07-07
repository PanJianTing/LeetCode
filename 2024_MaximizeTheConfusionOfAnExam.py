from collections import defaultdict, Counter

class Solution:
    def sliding(self, key, k, word) -> int:

        i = 0
        N = len(key)
        for j in range(N):
            if word != key[j]:
                k -= 1
            if k < 0:
                k += (word != key[i])
                i += 1
        return j - i + 1

    def maxConsecutiveAnswers(self, key, k) -> int:

        return max(self.sliding(key, k, "T"), self.sliding(key, k, "F"))
    

    def isValid(self, key, mid, k) -> bool:
        N = len(key)
        counter = defaultdict(int)

        for i in range(mid):
            counter[key[i]] += 1

        if min(counter['T'], counter['F']) <= k:
            return True
        
        for i in range(mid, N):
            counter[key[i]] += 1
            counter[key[i-mid]] -= 1

            if min(counter['T'], counter['F']) <= k:
                return True
            
        return False


    def maxConsecutiveAnswers(self, key, k) -> int:
        N = len(key)
        l = k
        r = N

        while l < r:
            mid = r - ((r-l) >> 1)

            if self.isValid(key, mid, k):
                l = mid
            else:
                r = mid - 1
        return l
    
    def maxConsecutiveAnswers(self, key, k) -> int:
        N = len(key)
        l = 0
        count = defaultdict(int)
        ans = k
        for i in range(k):
            count[key[i]] += 1

        for r in range(k, N):
            count[key[r]] += 1

            while min(count['T'], count['F']) > k:
                count[key[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
    
    def maxConsecutiveAnswers(self, key, k) -> int:
        maxf = 0
        res = 0
        counter = Counter()
        for i in range(len(key)):
            counter[key[i]] += 1
            maxf = max(maxf, counter[key[i]])
            if res - maxf < k:
                res += 1
            else:
                # 往左移
                counter[key[i-res]] -= 1
        return res
    
    def maxConsecutiveAnswers(self, key, k) -> int:
        N = len(key)
        maxf = 0
        i = 0
        count = Counter()
        for j in range(N):
            count[key[j]] += 1
            maxf = max(maxf, count[key[j]])
            if j - i + 1 > maxf + k:
                count[key[i]] -= 1
                i += 1
        return len(key) - i



    
print(Solution().maxConsecutiveAnswers("TTFF", 2))
print(Solution().maxConsecutiveAnswers("TFFT", 1))
print(Solution().maxConsecutiveAnswers("TTFTTFTT", 1))