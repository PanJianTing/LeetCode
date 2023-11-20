from collections import defaultdict

class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        ans = len("".join(garbage))
        garbage_dis = defaultdict(int)

        for i in range(1, len(travel)):
            travel[i] = travel[i-1] + travel[i]
        

        for i, h in enumerate(garbage):
            if "M" in h:
                garbage_dis["M"] = i
            
            if "G" in h:
                garbage_dis["G"] = i
            
            if "P" in h:
                garbage_dis["P"] = i
            
            # for t in h:
            #     garbage_dis[t] = i
                

        for t in "MGP":
            if garbage_dis[t] > 0:
                ans += travel[garbage_dis[t]-1]
                
        return ans
    

    def garbageCollection(self, garbage, travel) -> int:
        ans = len("".join(garbage))
        N = len(garbage)
        
        for i in range(N):
            garbage[i] = set(garbage[i])

        M = True
        P = True
        G = True
        for i in range(N-1, -1, -1):
            if M and "M" in garbage[i]:
                ans += sum(travel[:i])
                M = False

            if P and "P" in garbage[i]:
                ans += sum(travel[:i])
                P = False

            if G and "G" in garbage[i]:
                ans += sum(travel[:i])
                G = False

        return ans
    

print(Solution().garbageCollection(["G","P","GP","GG"], [2,4,3]))
print(Solution().garbageCollection(["MMM","PGM","GP"], [3,10]))
print(Solution().garbageCollection(["G","M"], [1]))