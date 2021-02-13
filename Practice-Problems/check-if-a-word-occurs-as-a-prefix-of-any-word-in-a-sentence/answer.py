class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        senLst = sentence.split()
        for i in range(len(senLst)):
            if searchWord == senLst[i][:len(searchWord)]:
                return i + 1
        return -1
