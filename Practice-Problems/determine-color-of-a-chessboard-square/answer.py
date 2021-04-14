class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dist = abs(ord(coordinates[0]) - ord("a")) + abs(int(coordinates[1]) - 1)
        if dist % 2 == 0:
            return False
        else: 
            return True
