class Solution:

    # Time -> O(n^2)
    # Space -> O(1)
    def maxProfit(self, prices: list[int]) -> int:

        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    # Time -> O(n)
    # Space -> O(1)
    def maxProfit(self, prices: list[int]) -> int:

        buy = prices[0]
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                max_profit = max(max_profit, price - buy)

        return max_profit
    

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,5,4,3,1]))