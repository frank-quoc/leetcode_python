class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = {}
        good_pairs = 0
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                good_pairs += nums_dict[nums[i]]
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        return good_pairs
