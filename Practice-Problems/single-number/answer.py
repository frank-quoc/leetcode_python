from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        for k, v in count_nums.items():
            if v == 1:
                return k
            
# Better Solution
# res = 0
# for num in nums:
#     res ^= num
# return num
