class Solution:
    def modifyString(self, s: str) -> str:
        alphabet = "abcedfghijklmnopqrstuvwxyz"
        if len(s) == 1:
            return "a" if s == "?" else s
        new_s = list(s)
        for i in range(len(new_s)):
            if new_s[i] == "?":
                for letter in alphabet:
                    if i == 0:
                        if new_s[i+1] != letter:
                            new_s[i] = letter
                    elif i == len(new_s) - 1:
                        if new_s[i-1] != letter:
                            new_s[i] = letter
                    elif new_s[i-1] != letter and new_s[i+1] != letter:
                        new_s[i] = letter
        return "".join(new_s)
