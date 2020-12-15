class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        rev_bin_n = bin_n[::-1]
        while len(rev_bin_n) < 32:
            rev_bin_n += '0'
        rev_n = int(rev_bin_n, 2)
        return rev_n
