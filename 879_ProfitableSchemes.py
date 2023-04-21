class Solution:
    mod = 10 ** 9 + 7
    memo = []

    def find(self, pos: int, count: int, profit: int, n: int, minProfit: int, group: list[int], profits: list[int]) -> int:
        if pos == len(group):
            return 1 if profit >= minProfit else 0
        
        if self.memo[pos][count][profit] != -1:
            return self.memo[pos][count][profit]
        
        totalWay = self.find(pos+1, count, profit, n, minProfit, group, profits)

        if (count + group[pos]) <= n:
            totalWay += self.find(pos+1, count + group[pos], 
                                  min(minProfit, profit + profits[pos]), n, minProfit, group, profits)
            
        self.memo[pos][count][profit] = totalWay

        return self.memo[pos][count][profit]



    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:

        self.memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

        return self.find(0,0,0, n, minProfit, group, profit) % self.mod

