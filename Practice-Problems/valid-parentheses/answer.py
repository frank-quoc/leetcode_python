class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {'(':')', '[':']', '{':'}'}
        for s_symbol in s:
            if s_symbol in symbols.keys(): # If it's an opener:
                stack.append(s_symbol)
            # Checks if the stack is empty or closing symbol matches opening symbol in stack
            elif not stack or (s_symbol != symbols[stack.pop()]):
                return False
        return stack == []
