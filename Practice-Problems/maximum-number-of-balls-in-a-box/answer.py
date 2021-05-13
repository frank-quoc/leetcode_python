class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count_dict = {} 
        for num in range(lowLimit, highLimit + 1):
            box = 0
            while num > 0:
                mod = num % 10 
                num = num // 10
                box += mod
            count_dict[box] = count_dict.get(box, 0) + 1
        return(max(count_dict.values()))
