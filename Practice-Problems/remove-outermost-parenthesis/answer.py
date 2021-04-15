class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        no_primitive = ""
        curr_string = ""
        for string in S:
            if string == "(":
                count += 1
                curr_string += string
            elif string == ")":
                count -= 1
                curr_string += string
            if count == 0:
                no_primitive += curr_string[1:-1]
                curr_string = ""
        return no_primitive
