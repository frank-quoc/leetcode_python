class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tot = sum(arr)
        for i in range(3, len(arr) + 1, 2):
            start = 0
            end = i
            while end <= len(arr):
                tot += sum(arr[start: end])
                start += 1
                end += 1
        return tot
