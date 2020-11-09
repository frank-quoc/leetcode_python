class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,'V':5, 'I': 1 }
        integer = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and rom_dict[s[i+1]] > rom_dict[s[i]]:
                integer -= rom_dict[s[i]]
            else:
                integer += rom_dict[s[i]]
        
        return integer
