class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        cur_drink = numBottles
        remaining_bottles = 0

        while cur_drink > 0:
            total += cur_drink
            remaining_bottles += cur_drink
            next_drink = remaining_bottles // numExchange
            remaining_bottles %= numExchange
            cur_drink = next_drink

        return total
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0

        while numBottles >= numExchange:

            numBottles = numBottles - numExchange + 1
            drink += numExchange
        
        return drink + numBottles
    
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        
        while numBottles >= numExchange:
            can_drink = numBottles // numExchange
            numBottles = numBottles - can_drink * numExchange + can_drink
            drink += can_drink * numExchange

        return drink + numBottles


print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))