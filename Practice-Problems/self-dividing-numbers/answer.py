class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            curr_num = num
            flag = True
            while curr_num > 0:
                remainder = curr_num % 10
                if remainder == 0 or num % remainder != 0:
                    flag = False
                    break
                curr_num //= 10
            if flag is True:
                res.append(num)
        return res
