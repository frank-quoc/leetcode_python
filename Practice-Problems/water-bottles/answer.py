class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinkBottles = numBottles
        while numBottles >= numExchange:
            drinkBottles += numBottles // numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange
        return drinkBottles
