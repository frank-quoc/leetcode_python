class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      return ((int(not(num)) for num in row[::-1]) for row in image)
