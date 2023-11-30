from functools import cache

class Solution:
    
    def numberOfWays(self, corridor) -> int:
        N = len(corridor)
        MOD = 10 ** 9 + 7
        wayCache = [[-1] * 3 for _ in range(N)]
        
        def dp(cur, seat):
            if cur == N: 
                if seat == 2:
                    return 1
                return 0
            
            if wayCache[cur][seat] != -1:
                return wayCache[cur][seat]
            
            res = 0
            if "S" == corridor[cur]:
                if seat == 2:
                    res = dp(cur+1, 1)
                else:
                    res = dp(cur + 1, seat + 1)
            else:
                if seat == 2:
                    res = dp(cur+1, seat) + dp(cur+1, 0)
                else:
                    res = dp(cur+1, seat)

            wayCache[cur][seat] = res
            return wayCache[cur][seat]
        
        return dp(0,0) % MOD
    

    def numberOfWays(self, s) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        dp = [[0] * 3 for _ in range(N+1)]

        dp[N][2] = 1

        for i in range(N-1, -1, -1):
            if s[i] == "S":
                dp[i][0] = dp[i+1][1]
                dp[i][1] = dp[i+1][2]
                dp[i][2] = dp[i+1][1]
            else:
                dp[i][0] = dp[i+1][0]
                dp[i][1] = dp[i+1][1]
                dp[i][2] = dp[i+1][0] + dp[i+1][2]

        return dp[0][0] % MOD
    
    def numberOfWays(self, s) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        dp = [0] * 3
        dp[2] = 1

        for i in range(N-1, -1, -1):
            next = [0]*3
            if s[i] == "S":
                next[0] = dp[1]
                next[1] = dp[2]
                next[2] = dp[1]
            else:
                next[0] = dp[0]
                next[1] = dp[1]
                next[2] = dp[0] + dp[2]
            dp = next

        return dp[0] % MOD
    
    def numberOfWays(self, s) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        zero = 0
        one = 0
        two = 1

        for i in range(N-1, -1, -1):
            if s[i] == "S":
                zero = one
                one, two = two, one
            else:
                two += zero

        return zero % MOD
    
    def numberOfWays(self, s) -> int:
        MOD = 10 ** 9 + 7
        idxes = []
        for i, c in enumerate(s):
            if c == 'S':
                idxes.append(i)

        if len(idxes) % 2:
            return 0
        
        idx1 = 1
        idx2 = 2
        ans = 1
        while idx2 < len(idxes):
            ans *= (idxes[idx2] - idxes[idx1])
            idx1 += 2
            idx2 += 2
        return ans % MOD
    
    def numberOfWays(self, s) -> int:
        MOD = 10 ** 9 + 7
        last_pair_idx = None
        seat = 0
        ans = 1
        for i, c in enumerate(s):
            if c == "S":
                seat += 1
                if seat == 2:
                    last_pair_idx = i
                    seat = 0
                elif seat == 1 and last_pair_idx != None:
                    ans = ans * (i - last_pair_idx)

        if last_pair_idx == None or seat == 1:
            return 0
        return ans % MOD
                


# print(Solution().numberOfWays("SSPPSPS"))
# print(Solution().numberOfWays("PPSPSP"))
# print(Solution().numberOfWays("S"))
                     
# print(Solution().numberOfWays("PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"))
print(Solution().numberOfWays("SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"))
                     
        