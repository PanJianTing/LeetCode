class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        M = len(bank)
        N = len(bank[0])
        ans = 0
        be = 0

        for i in range(M):
            cnt = 0
            for j in range(N):
                if bank[i][j] == '1':
                    cnt += 1
            if cnt == 0:
                continue
            ans += be * cnt
            be = cnt
        return ans
    
    def numberOfBeams(self, bank: list[str]) -> int:
        N = len(bank)
        device = []
        ans = 0
        for i in range(N):
            cnt = bank[i].count('1')
            if cnt > 0:
                device.append(cnt)
        for i in range(1, len(device)):
            ans += device[i] * device[i-1]
        return ans
    
print(Solution().numberOfBeams(["011001","000000","010100","001000"]))
print(Solution().numberOfBeams(["000","111","000"]))
# print(Solution().numberOfBeams(["011001","000000","010100","001000"]))