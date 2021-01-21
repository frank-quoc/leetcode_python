class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        repeats = 0
        for i in range(len(sequence) + 1):
            if word * i in sequence:
                repeats = i
        return repeats
