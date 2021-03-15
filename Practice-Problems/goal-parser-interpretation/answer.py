class Solution:
    def interpret(self, command: str) -> str:
        # parsed = ""
        # i = 0
        # while i < len(command):
        #     if command[i] == "G":
        #         parsed += "G"
        #         i += 1
        #     elif command[i] == "(":
        #         if command[i + 1]  == ")":
        #             parsed += "o"
        #             i += 2
        #         else:
        #             parsed += "al"
        #             i += 4
        # return parsed
        return command.replace("()", "o").replace("(al)", "al")
