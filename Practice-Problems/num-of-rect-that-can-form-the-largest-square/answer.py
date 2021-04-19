class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = [min(sides) for sides in rectangles]
        return squares.count(max(squares))
