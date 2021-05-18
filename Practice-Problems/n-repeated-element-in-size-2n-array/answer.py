class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for num in A:
            if A.count(num) == len(A) / 2:
                return num
