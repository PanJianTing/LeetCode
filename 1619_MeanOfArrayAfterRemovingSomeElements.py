class Solution:
    # 移除最大的5%個數與最小的5%的數
    def trimMean(self, arr: list[int]) -> float:

        removeLen = int(0.05*len(arr))
        arr = sorted(arr)
        arr = arr[removeLen:-(removeLen)]

        return sum(arr) / len(arr)

        
# print(Solution.trimMean(Solution(), [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))
print(Solution.trimMean(Solution(), [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))