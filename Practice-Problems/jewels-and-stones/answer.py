class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_in_stones = 0
        for stone in stones:
            if stone in jewels:
                jewels_in_stones += 1
        return jewels_in_stones
