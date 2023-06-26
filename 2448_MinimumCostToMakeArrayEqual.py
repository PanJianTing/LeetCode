from collections import defaultdict

class Solution:
    
    # solution #1 prefix sum
    def minCost(self, num, cost) -> int:
        
        numCost = []
        N = len(num)
        for n, c in zip(num, cost):
            numCost.append((n,c))
        numCost = sorted(numCost, key=lambda x: x[0])

        prefix = [0] * N
        prefix[0] = numCost[0][1]
        for i in range(1, N):
            prefix[i] = numCost[i][1] + prefix[i-1]

        ans = 0
        for i in range(N):
            ans += numCost[i][1] * (numCost[i][0] - numCost[0][0])
        
        total = ans
        for i in range(1, N):
            gap = numCost[i][0] - numCost[i-1][0]
            total += gap * prefix[i-1]
            total -= gap * (prefix[N-1] - prefix[i-1])
            ans = min(ans, total)
        
        return ans
    

    # solution #2 BS
    def minCost(self, num, cost) -> int:

        def get_cost(base):
            return sum(abs(n-base) * c for n, c in zip(num, cost))
        
        l = min(num)
        r = max(num)
        ans = get_cost(num[0])

        while l < r:
            m = (l + r) >> 1
            cost1 = get_cost(m)
            cost2 = get_cost(m+1)
            ans = min(cost1, cost2)

            if cost1 > cost2:
                l = m + 1
            else:
                r = m

        return ans
            

print(Solution().minCost([1,3,5,2], [2,3,1,14]))
print(Solution().minCost([735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518], 
                         [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]))

