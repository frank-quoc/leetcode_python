class Solution:
    def generateTheString(self, n: int) -> str:
        string = (n-1) * "a"
        string += "a" if n & 1 else "b"
        return string
