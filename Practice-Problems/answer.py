class Solution:
    def maxDepth(self, s: str) -> int:
        depth = [0]
        count = 0
        for charc in s:
            if charc == "(":
                count += 1
                depth.append(count)
            elif charc == ")":
                count -= 1
        return max(depth)
