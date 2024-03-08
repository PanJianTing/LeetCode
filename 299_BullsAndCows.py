from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        N = len(secret)
        s_cnt = defaultdict(int)
        g_cnt = defaultdict(int)
        cow = 0
        bull = 0

        for i in range(N):
            s_cnt[secret[i]] += 1
            g_cnt[guess[i]] += 1
        
        for k in s_cnt:
            cow += min(s_cnt[k], g_cnt[k])
        
        for i in range(N):
            if secret[i] == guess[i]:
                cow -= 1
                bull += 1

        return f'{bull}A{cow}B'
    

    def getHint(self, secret: str, guess: str) -> str:
        N = len(secret)
        s_cnt = defaultdict(int)
        cow = 0
        bull = 0

        for i in range(N):
            s_cnt[secret[i]] += 1
        
        for i in range(N):
            cur_gc = guess[i]
            if cur_gc in s_cnt:
                if secret[i] == cur_gc:
                    bull += 1
                    if s_cnt[secret[i]] <= 0:
                        cow -= 1
                else:
                    if s_cnt[cur_gc] > 0:
                        cow += 1
                s_cnt[cur_gc] -= 1
        
        return f'{bull}A{cow}B'
    

    def getHint(self, secret: str, guess: str) -> str:
        cnt_map = defaultdict(int)
        bull = 0
        cow = 0
        for s,g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                '''
                Our correcte number in map less than 0,
                Represent we have guessed the number but not correct position before,
                so, cow plus += 1
                '''
                if cnt_map[s] < 0:
                    cow += 1
                '''
                Our guess number in map over than 0, 
                Represent we have correcte number but not correct position before,
                so, cow plus 1 
                '''
                if cnt_map[g] > 0:
                    cow += 1

                cnt_map[s] += 1
                cnt_map[g] -= 1

        return f'{bull}A{cow}B'
        
    

print(Solution().getHint('1123', '0111'))
print(Solution().getHint('1807', '7810'))
print(Solution().getHint('7810', '1870'))
        