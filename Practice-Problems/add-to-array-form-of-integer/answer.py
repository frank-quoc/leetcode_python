class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        str_num = ''.join(map(str, A))
        sum_num = int(str_num) + K
        lst_sum = list(str(sum_num))
        return lst_sum
