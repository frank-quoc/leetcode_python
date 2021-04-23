class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        counter = {}
        for charc in s:
            counter[charc] = counter.get(charc, 0) + 1
        
        reverse = False
        while counter:
            for charc in dict(sorted(counter.items(), reverse=reverse)):
                result += charc
                counter[charc] -= 1
                if not counter[charc]:
                    del counter[charc]
            reverse = not reverse
        return result
        
