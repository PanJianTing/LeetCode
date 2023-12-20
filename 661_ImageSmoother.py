class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        M = len(img)
        N = len(img[0])
        ans = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                cnt = 0
                all_sum = 0
                for curI in range(max(i-1, 0), min(i+1+1, M)):
                    for curJ in range(max(j-1, 0), min(j+1+1, N)):
                        cnt += 1
                        all_sum += img[curI][curJ]
                ans[i][j] = all_sum // cnt
        return ans

    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        M = len(img)
        N = len(img[0])
        
        temp = [0] * N
        temp_val = 0

        for i in range(M):
            for j in range(N):
                all_sum = img[i][j]
                cnt = 1
                if i + 1 < M:
                    for curJ in [j-1, j, j+1]:
                        if 0 <= curJ < N:
                            all_sum += img[i+1][curJ]
                            cnt += 1
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        all_sum += temp_val
                        cnt += 1
                    
                    for curJ in [j, j + 1]:
                        if 0 <= curJ < N:
                            all_sum += temp[curJ]
                            cnt += 1
                if j + 1 < N:
                    all_sum += img[i][j+1]
                    cnt += 1

                if j - 1 >= 0:
                    all_sum += temp[j-1]
                    cnt += 1

                if i-1 >= 0:
                    temp_val = temp[j]

                temp[j] = img[i][j]

                img[i][j] = all_sum // cnt
        return img



    
print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))