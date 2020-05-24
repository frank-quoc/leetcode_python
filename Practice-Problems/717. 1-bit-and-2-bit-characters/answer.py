class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        answer = []
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                answer.append(2)
                i += 2
            else:
                answer.append(1)
                i += 1
                
        if answer[-1] == 1:
            return True
        else:
            return False
