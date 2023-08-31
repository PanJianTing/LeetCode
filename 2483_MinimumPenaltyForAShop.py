class Solution:
    def bestClosingTime(self, c) -> int:
        N = len(c)
        closeTime = N+1
        currPenalty = N+1

        for time in range(0, N+1):
            penalty = 0
            for i, have in enumerate(c):
                if i < time:
                    if have == "N":
                        penalty += 1
                else:
                    if have == "Y":
                        penalty += 1
            
            # print(time, penalty)
            if penalty < currPenalty:
                closeTime = time
                currPenalty = penalty

        return closeTime
    
    def bestClosingTime(self, c):
        N = len(c)

        currPenalty = 0
        smallPanalty = 0
        currTime = N

        for have in c:
            if have == "N":
                currPenalty += 1
        smallPanalty = currPenalty
        
        for time in range(N-1, -1, -1):
            
            if c[time] == "Y":
                currPenalty += 1
            else:
                currPenalty -= 1
            
            if currPenalty <= smallPanalty:
                currTime = time
                smallPanalty = currPenalty
            
        return currTime
    
    def bestClosingTime(self, c):
        N = len(c)
        smallest = 0
        time = 0
        
        for have in c:

            if have == "Y":
                smallest += 1
        
        curr = smallest
        for t in range(1, N+1):
            
            if c[t-1] == "Y":
                curr -= 1
            else:
                curr += 1
            
            if curr < smallest:
                time = t
                smallest = curr
            
        return time
                





            
        

print(Solution().bestClosingTime("YYNY"))
print(Solution().bestClosingTime("NNNN"))
print(Solution().bestClosingTime("YYYY"))
print(Solution().bestClosingTime("YNYY"))