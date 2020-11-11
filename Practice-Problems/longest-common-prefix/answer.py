class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = ""
            strs = sorted(strs, key=len)
            # Iterate through the shortest str
            for i in range(len(strs[0])):
                letter = strs[0][i]

                # Iterate through the list, except the shortest str
                for j in range(1, len(strs)):
                    # if any of the prefix letters don't match, return the prefix
                    if strs[j][i] != letter:
                        return prefix
                
                prefix += letter
            return prefix
