class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for col in range(len(matrix[0])):
            trans_row = []
            for row in range(len(matrix)):
                trans_row.append(matrix[row][col])
            transpose.append(trans_row)
        return transpose
