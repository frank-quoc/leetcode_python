class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        i = 0
        j = len(mat) - 1
        for row in mat:
            if i != j:
                diag_sum += row[i] + row[j]
            else:
                diag_sum += row[i]
            i += 1
            j -= 1
        return diag_sum
