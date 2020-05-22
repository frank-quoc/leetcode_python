# My solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
# More efficient solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        computed_sum = {}
        for i in range(0, len(nums)):
            required = target - nums[i]
            if required in computed_sum: 
                return [computed_sum[required], i]
            computed_sum[nums[i]] = i
        return []
