class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1, max_2 = 0, 0
        max_1 = max(nums)
        nums.remove(max(nums))
        max_2 = max(nums)
        nums.remove(max(nums))
        return (max_1 - 1) * (max_2 - 1)
