class Solution:
    def freqAlphabets(self, s: str) -> str:
        code = ""
        i = len(s) - 1
        while i > -1:
            if s[i] == "#":
                code += chr(int(s[i-2:i])+96)
                i -= 3
            else:
                code += chr(int(s[i])+96)
                i -= 1
        return code[::-1]
